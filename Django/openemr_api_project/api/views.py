from django.contrib.auth.models import User
from models import PatientData, MedicalHistory, Forms, FormEncounter
from rest_framework import viewsets
from serializers import UserSerializer, PatientDataSerializer, ListMedicalHistorySerializer, CreateUpdateMedicalHistorySerializer, FormsSerializer, FormEncounterSerializer
from django.shortcuts import render_to_response
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import status
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
		pd_cache_query = str("PD-" + public_pid)
		cached = cache.get(pd_cache_query)
		if cached:
			return MedicalHistory.objects.filter(pid=int(cached[0].pid))
		else:
			queryset = MedicalHistory.objects.filter(patient_data__pubpid=public_pid)
			cache.set(pd_cache_query, queryset, 3600)
			return queryset



@api_view(['GET'])
def visits_list(request, pubpid, format=None):
	"""
	Function based view to return flat representation of patient visits.
	:param request: HTTP Request
	:param pubpid: Public patient id, used to perform queries
	:param format: .json or .api
	:return: dict of patients visit history
	"""

	#try:
	#patient = PatientData.objects.all()

	#if request.method == 'GET':

	return Response(status=status.HTTP_200_OK)


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
			cache_query = str("PD-" + pubpid)
			cached = cache.get(cache_query)
			if not cached:
				queryset = queryset.filter(pubpid=pubpid)
				cache.set(cache_query, queryset, 3600)
			else:
				queryset = cached
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