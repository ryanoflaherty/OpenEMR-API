from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import PatientData, HistoryData, MedicalHistory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class HistoryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryData


class PatientDataSerializer(serializers.ModelSerializer):
    pid = serializers.IntegerField()
    pubpid = serializers.CharField()
    ss = serializers.CharField()
    date = serializers.DateTimeField()
    fname = serializers.CharField()
    lname = serializers.CharField()
    mname = serializers.CharField()
    dob = serializers.DateField()
    sex = serializers.CharField()
    status = serializers.CharField()
    email = serializers.CharField()
    street = serializers.CharField()
    postal_code = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    country_code = serializers.CharField()
    phone_contact = serializers.CharField()
    phone_cell = serializers.CharField()

    class Meta:
        model = PatientData
        exclude = ('med_his',)


class MedicalHistorySerializer(serializers.ModelSerializer):
    history_data = HistoryDataSerializer(many=True)
    patient_data = PatientDataSerializer()
    #history_data = HistoryDataSerializer
    class Meta:
        model = MedicalHistory

'''
pid = serializers.IntegerField(source='patientdata.pid')
    pubpid = serializers.CharField(source='patientdata.pubpid')
    ss = serializers.CharField(source='patientdata.ss')
    date = serializers.DateTimeField(source='patientdata.date')
    fname = serializers.CharField(source='patientdata.fname')
    lname = serializers.CharField(source='patientdata.lname')
    mname = serializers.CharField(source='patientdata.mname')
    dob = serializers.DateField(source='patientdata.dob')
    sex = serializers.CharField(source='patientdata.sex')
    status = serializers.CharField(source='patientdata.status')
    email = serializers.CharField(source='patientdata.email')
    street = serializers.CharField(source='patientdata.street')
    postal_code = serializers.CharField(source='patientdata.postal_code')
    city = serializers.CharField(source='patientdata.city')
    state = serializers.CharField(source='patientdata.state')
    country_code = serializers.CharField(source='patientdata.country_code')
    phone_contact = serializers.CharField(source='patientdata.phone_contact')
    phone_cell = serializers.CharField(source='patientdata.phone_cell')
'''