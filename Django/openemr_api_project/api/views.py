from django.shortcuts import render
from django.contrib.auth.models import User, Group
from api.models import PatientData, HistoryData, MedicalHistory
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, PatientDataSerializer, HistoryDataSerializer, MedicalHistorySerializer
from django.template import RequestContext
from django.shortcuts import render_to_response
from rest_framework import filters, generics
from rest_framework import authentication, permissions


def index(request):
		return render_to_response('bootstrap/index.html')


class UserViewSet(viewsets.ModelViewSet):
	# API endpoint that allows users to be viewed or deleted
	queryset = User.objects.all()
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	# API endpoint that allows groups to be viewed or edited
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class PatientDataViewSet(viewsets.ModelViewSet):
	# API endpoint for patient data to be viewed or added to
	queryset = PatientData.objects.all()
	serializer_class = PatientDataSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('pid', 'pubpid', 'ss', 'fname', 'lname', 'mname', 'dob', 'sex', 'status', 'email', 'street', 'postal_code', 'city', 'state', 'country_code')


class HistoryDataViewSet(viewsets.ModelViewSet):
	# API endpoint for patient data to be viewed or added to
	queryset = HistoryData.objects.all()
	serializer_class = HistoryDataSerializer


class MedicalHistoryViewSet(viewsets.ModelViewSet):
	queryset = MedicalHistory.objects.all()
	serializer_class = MedicalHistorySerializer


class HistoryDataList(generics.ListAPIView):
	serializer_class = HistoryDataSerializer
	#authentication_classes = (authentication.TokenAuthentication)
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly)

	def get_queryset(self):
		pid = self.kwargs['pid']
		return HistoryData.objects.filter(pid=pid)

class PatientDataList(generics.ListAPIView):
	serializer_class = PatientDataSerializer
	queryset = PatientData.objects.all()
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('fname', 'lname',)
