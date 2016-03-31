from django.contrib.auth.models import User, Group
from models import PatientData, HistoryData, MedicalHistory, Forms, FormEncounter
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, PatientDataSerializer, HistoryDataSerializer, MedicalHistorySerializer, FormsSerializer, FormEncounterSerializer
from django.shortcuts import render_to_response
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


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
		'records': reverse('medical-record-create-update', request=request, format=format),
		'records/patient-data': reverse('patient-data-list', request=request, format=format),
		'records/{pubpid}/visits': reverse('visits-list', request=request, format=format, kwargs={'pubpid': '123'}),
		'records/{pid}/history-data': reverse('history-data-list', request=request, format=format, kwargs={'pid':1}),
		#'users': reverse('users', request=request, format=format),
		#'groups': reverse('groups', request=request, format=format),
	})


class HistoryDataList(generics.ListAPIView):
	"""
	This view allow the user to use .list() or .retrieve() for history data based on the users pid.
	"""
	serializer_class = HistoryDataSerializer

	def get_queryset(self):
		pid = self.kwargs['pid']
		return HistoryData.objects.filter(pid=pid)


class VisitsHistoryList(generics.ListAPIView):
	"""
	This view allow the user to use .list() or .retrieve() for patient visits data based on the users pubpid.
	"""
	serializer_class = MedicalHistorySerializer

	def get_queryset(self):
		public_pid = self.kwargs['pubpid']
		return MedicalHistory.objects.filter(patient_data__pubpid=public_pid)


class PatientDataList(generics.ListAPIView):
	"""
	This view allow the user to use .list() or .retrieve() for patient data, as well as search by all fields.
	"""
	serializer_class = PatientDataSerializer
	queryset = PatientData.objects.all()
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('pid', 'pubpid', 'ss', 'fname', 'lname', 'mname', 'dob', 'sex', 'status', 'email', 'street', 'postal_code', 'city', 'state', 'country_code')


class CreateUpdateMedicalRecord(generics.ListCreateAPIView, generics.UpdateAPIView):
	"""
	This view allow the user to view and modify MedicalHistory records.
	"""
	queryset = MedicalHistory.objects.all()
	serializer_class = MedicalHistorySerializer


class UserViewSet(viewsets.ModelViewSet):
	"""
	This view allow the user to view and modify users.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	This view allow the user to view and modify groups.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class FormsList(generics.ListAPIView):
	queryset = Forms.objects.all()
	serializer_class = FormsSerializer