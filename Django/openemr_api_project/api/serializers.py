from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import PatientData, HistoryData

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')


class PatientDataSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PatientData
		read_only_fields = ('dob', 'ss', 'pid')

class HistoryDataSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = HistoryData
