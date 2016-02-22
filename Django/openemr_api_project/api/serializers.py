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


class HistoryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryData
        fields = (
            'date',
            'pid',
            'tobacco',
        )

class PatientDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientData
        fields = (
			'fname',
			'lname',
			'date',
        )
