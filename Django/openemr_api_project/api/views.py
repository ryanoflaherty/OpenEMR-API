from django.shortcuts import render
from django.contrib.auth.models import User, Group
from api.models import PatientData, HistoryData
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, PatientDataSerializer, HistoryDataSerializer
from django.template import RequestContext
from django.shortcuts import render_to_response


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
	# API endpoint for patient data to be viewd or added to
	queryset = PatientData.objects.all()
	serializer_class = PatientDataSerializer

class HistoryDataViewSet(viewsets.ModelViewSet):
	# API endpoint for patient data to be viewed or added to
	queryset = HistoryData.objects.all()
	serializer_class = HistoryDataSerializer

