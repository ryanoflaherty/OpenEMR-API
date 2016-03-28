from django.shortcuts import render
from django.contrib.auth.models import User, Group
from api.models import PatientData, HistoryData, MedicalHistory
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, PatientDataSerializer, HistoryDataSerializer, MedicalHistorySerializer
from django.template import RequestContext
from django.shortcuts import render_to_response
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


"""
This view returns the homepage to the user.
"""


def index(request):
		return render_to_response('bootstrap/index.html')


"""
This view constructs the API root for browsable API.
"""
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'records/patient-data': reverse('patient-data-list', request=request, format=format),
        'records/pid/history-data': reverse('history-data-list', request=request, format=format, kwargs={'pid':1})
    })

"""
This view allow the user to use .list() or .retrieve() for history data based on the users pid.
"""


class HistoryDataList(generics.ListAPIView):
	serializer_class = HistoryDataSerializer

	def get_queryset(self):
		pid = self.kwargs['pid']
		return HistoryData.objects.filter(pid=pid)


"""
This view allow the user to use .list() or .retrieve() for patient data, as well as search by all fields.
"""


class PatientDataList(generics.ListAPIView):
	serializer_class = PatientDataSerializer
	queryset = PatientData.objects.all()
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('pid', 'pubpid', 'ss', 'fname', 'lname', 'mname', 'dob', 'sex', 'status', 'email', 'street', 'postal_code', 'city', 'state', 'country_code')


"""
This view allow the user to view and modify MedicalHistory records.
"""


class MedicalHistoryViewSet(viewsets.ModelViewSet):
	queryset = MedicalHistory.objects.all()
	serializer_class = MedicalHistorySerializer


"""
This view allow the user to view and modify users.
"""


class UserViewSet(viewsets.ModelViewSet):
	# API endpoint that allows users to be viewed or deleted
	queryset = User.objects.all()
	serializer_class = UserSerializer


"""
This view allow the user to view and modify groups.
"""


class GroupViewSet(viewsets.ModelViewSet):
	# API endpoint that allows groups to be viewed or edited
	queryset = Group.objects.all()
	serializer_class = GroupSerializer