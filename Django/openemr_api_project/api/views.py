from django.contrib.auth.models import User
from models import PatientData, MedicalHistory, Forms, HistoryData, Visit
from rest_framework import viewsets
from serializers import UserSerializer, PatientDataSerializer, ListMedicalHistorySerializer, CreateUpdateMedicalHistorySerializer, FormsSerializer, HistoryDataSerializer, VisitSerializer

from django.shortcuts import render_to_response
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.core.cache import cache


def index(request):
	"""
	This view returns the homepage to the user.
	"""
	return render_to_response('bootstrap/index.html')


@api_view(['GET'])
def api_root(request, format=None):
	"""
	This view constructs the API root for browsable API.
	"""
	return Response({
		'records/': reverse('medical-record-create-update', request=request, format=format),
		'records/patient-data': reverse('patient-data-list', request=request, format=format),
		'records/{pubpid}/visits': reverse('visits-list', request=request, format=format, kwargs={'pubpid': '28005573'}),
		#'users': reverse('users', request=request, format=format),
	})


class VisitsHistoryList(generics.ListAPIView):
	"""
	This view allow the user to use .list() or .retrieve() for patient visits data based on the users pubpid.
	"""
	serializer_class = ListMedicalHistorySerializer

	def get_queryset(self):
		public_pid = self.kwargs['pubpid']
		return MedicalHistory.objects.filter(patient_data__pubpid=public_pid)
	"""
	def get_queryset(self):
		public_pid = self.kwargs['pubpid']
		mh_cache_query = str("MH-" + public_pid)
		cached = cache.get(mh_cache_query)
		if cached:
			return cached
		else:
			queryset = MedicalHistory.objects.filter(patient_data__pubpid=public_pid)
			cache.set(mh_cache_query, queryset, 3600)
			return queryset
	"""



@api_view(['GET'])
def visits_list(request, pubpid, format=None):
	"""
	Function based view to return flat representation of patient visits.
	:param request: HTTP Request
	:param pubpid: Public patient id, used to perform queries
	:param format: .json or .api
	:return: dict of patients visit history
	"""

	med_his = cache.get(str("MH-" + pubpid))

	if med_his:
		history_data = HistoryData.objects.filter(pid=med_his.pid).latest('date')
		#forms = Forms.objects.prefetch_related('form_reviewofs', 'form_ros', 'form_vitals').filter(pid=med_his.pid)
		forms = Forms.objects.filter(pid=med_his.pid)
	else:
		med_his = MedicalHistory.objects.get(patient_data__pubpid=pubpid)
		history_data = HistoryData.objects.filter(pid=med_his.pid).latest('date')
		forms = Forms.objects.filter(pid=med_his.pid)

	# Create dictionary to serialize
	visits = []
	dict = {}
	for form in forms:
		if str(form.encounter) not in dict:
			dict[str(form.encounter)] = len(visits)
			visits.append({"date": form.date, "user": form.user})
		if form.form_name == "Vitals":
			visits[dict[str(form.encounter)]]["glucose"] = form.form_vitals.glucose
			visits[dict[str(form.encounter)]]["pulse"] = form.form_vitals.pulse
			visits[dict[str(form.encounter)]]["bps"] = form.form_vitals.bps
			visits[dict[str(form.encounter)]]["bpd"] = form.form_vitals.bpd
			visits[dict[str(form.encounter)]]["height"] = form.form_vitals.height
			visits[dict[str(form.encounter)]]["weight"] = form.form_vitals.weight
			visits[dict[str(form.encounter)]]["bmi"] = form.form_vitals.bmi
		if form.form_name == "Review of Systems Checks":
			visits[dict[str(form.encounter)]]['dry_mouth'] = form.form_reviewofs.dry_mouth
			visits[dict[str(form.encounter)]]['high_blood_pressure'] = form.form_reviewofs.high_blood_pressure
		if form.form_name == "Review Of Systems":
			visits[dict[str(form.encounter)]]['numbness'] = form.form_ros.n_numbness
			visits[dict[str(form.encounter)]]['pregnant'] = form.form_ros.p
			visits[dict[str(form.encounter)]]['dizziness'] = form.form_ros.n_weakness
			visits[dict[str(form.encounter)]]['diabetes'] = form.form_ros.diabetes

	if request.method == 'GET':
		history_data_serializer = HistoryDataSerializer(history_data)

		serializer = {
			'history_data': history_data_serializer.data,
			'visits': visits,
		}
		return Response(serializer)


class PatientDataList(generics.ListAPIView):
	"""
	This view allow the user to use .list() or .retrieve() for patient data, as well as search by all fields.

	Since this is the first class accessed, cache Visits when accessed
	"""
	serializer_class = PatientDataSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('pid', 'pubpid', 'ss', 'fname', 'lname', 'mname', 'dob', 'sex', 'status', 'email', 'street', 'postal_code', 'city', 'state', 'country_code')

	def get_queryset(self):
		pubpid = self.request.query_params.get('pubpid', None)
		queryset = PatientData.objects.all()

		if pubpid is not None:
			queryset = queryset.filter(pubpid=pubpid)
			pd_cache_query = str("PD-" + pubpid)
			pd_cached = cache.get(pd_cache_query)

			if not pd_cached:
				cache.set(pd_cache_query, queryset, 3600)
				for q in queryset:
					related = MedicalHistory.objects.prefetch_related('forms', 'history_data').filter(pid=q.pid.pid)
					cache.set('MH-' + str(pubpid), related[0])

		return queryset


class CreateUpdateMedicalRecord(generics.CreateAPIView, generics.UpdateAPIView):
	"""
	This view allow the user to view and modify MedicalHistory records.
	"""
	queryset = MedicalHistory.objects.all()
	serializer_class = CreateUpdateMedicalHistorySerializer


class UserViewSet(viewsets.ModelViewSet):
	"""
	This view allow the user to view and modify users.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class FormsList(generics.ListAPIView):
	queryset = Forms.objects.all()
	serializer_class = FormsSerializer