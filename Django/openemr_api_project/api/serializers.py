from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import PatientData, HistoryData, MedicalHistory, FormEncounter, Forms, Lists, Facility, FormRos, FormReviewofs, FormVitals


# Users and Groups
#################################################
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# Facility, FormEncounter, FormRos, FormVitals, FormReviewofs
#####################################################
class FacilitySerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Facility


class FormEncounterSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    facility = FacilitySerializer(source='facility_id')

    class Meta:
        model = FormEncounter


class FormRosSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = FormRos


class FormVitalsSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = FormVitals


class FormReviewofsSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = FormReviewofs


# Forms, List, HistoryData, PatientData
##################################################
class FormsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField()
    encounter = serializers.IntegerField()
    form_name = serializers.CharField()
    pid = serializers.IntegerField()
    user = serializers.CharField(max_length=255)
    deleted = serializers.IntegerField(default=0)

    # Inherited
    form_encounter = FormRosSerializer()
    form_ros = FormRosSerializer()
    form_vitals = FormVitalsSerializer()
    form_reviewofs = FormReviewofsSerializer()

    class Meta:
        model = Forms
        #fields = ('id', 'date', 'encounter', 'form_name', 'pid', 'user', 'deleted', 'form_encounter', 'form_ros', 'form_reviewofs', 'form_vitals')


class HistoryDataSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.DateTimeField()
    pid = serializers.IntegerField()
    tobacco = serializers.CharField()
    relatives_diabetes = serializers.CharField()
    relatives_high_blood_pressure = serializers.CharField()

    class Meta:
        model = HistoryData


class ListsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lists


class PatientDataSerializer(serializers.ModelSerializer):
    pubpid = serializers.CharField()
    gov_id = serializers.CharField(source='ss')
    date = serializers.DateTimeField()
    fname = serializers.CharField()
    lname = serializers.CharField()
    mname = serializers.CharField()
    dob = serializers.DateField()
    sex = serializers.ChoiceField(choices=('Male', 'Female'))
    status = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField(source='street')
    postal_code = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    country_code = serializers.CharField()
    phone_contact = serializers.CharField()
    phone_cell = serializers.CharField()

    class Meta:
        model = PatientData
        exclude = ('street', 'ss', 'pid')


# MedicalHistory
###########################################################
class MedicalHistorySerializer(serializers.ModelSerializer):
    pid = serializers.IntegerField()
    history_data = serializers.SerializerMethodField(method_name='hsearch_by_pid') # HistoryDataSerializer(many=True)
    #patient_data = PatientDataSerializer()
    forms = serializers.SerializerMethodField(method_name='fsearch_by_pid') # FormsSerializer(many=True)
    lists = serializers.SerializerMethodField(method_name='lsearch_by_pid') # ListsSerializer(many=True)

    class Meta:
        model = MedicalHistory
        #depth = 5
        exclude = ('id',)

    def hsearch_by_pid(self, MedicalHistory):
        visit = HistoryData.objects.filter(pid=MedicalHistory.pid)
        serializer = HistoryDataSerializer(instance=visit, many=True)
        return serializer.data

    def fsearch_by_pid(self, MedicalHistory):
        visit = Forms.objects.filter(pid=MedicalHistory.pid)
        serializer = FormsSerializer(instance=visit, many=True)
        return serializer.data

    def lsearch_by_pid(self, MedicalHistory):
        visit = Lists.objects.filter(pid=MedicalHistory.pid)
        serializer = ListsSerializer(instance=visit, many=True)
        return serializer.data