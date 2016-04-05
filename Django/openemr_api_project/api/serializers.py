from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import PatientData, HistoryData, MedicalHistory, FormEncounter, Forms, Lists, Facility, FormRos, FormReviewofs, FormVitals
from rest_framework.fields import SkipField
from collections import OrderedDict


# Helper Class
class NonNullSerializer(serializers.Serializer):
    """
    Use this to prevent null response fields from being serialized
    """
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represention = field.to_representation(attribute)
                if represention is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represention, list) and not represention:
                   # Do not serialize empty lists
                   continue
                ret[field.field_name] = represention

        return ret


# Users and Groups
#################################################
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


# Facility, FormEncounter, FormRos, FormVitals, FormReviewofs
#####################################################
class FacilitySerializer(serializers.Serializer):
    #id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=30)
    fax = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=50)
    country_code = serializers.CharField(max_length=10)
    facility_npi = serializers.CharField(max_length=15)
    service_location = serializers.IntegerField()
    billing_location = serializers.IntegerField()
    color = serializers.CharField(max_length=7)

    class Meta:
        model = Facility


class FormEncounterSerializer(serializers.Serializer):
    #id = serializers.PrimaryKeyRelatedField(read_only=True)
    facility_id = serializers.PrimaryKeyRelatedField(read_only=True) # FacilitySerializer()
    date = serializers.DateTimeField()
    encounter = serializers.IntegerField()

    class Meta:
        model = FormEncounter


class FormRosSerializer(serializers.Serializer):
    #id = serializers.PrimaryKeyRelatedField(read_only=True)
    date = serializers.DateTimeField()
    p = serializers.CharField(max_length=3)
    n_numbness = serializers.CharField(max_length=3)
    n_weakness = serializers.CharField(max_length=3)
    diabetes = serializers.CharField(max_length=3)

    class Meta:
        model = FormRos


class FormVitalsSerializer(serializers.Serializer):
    #id = serializers.PrimaryKeyRelatedField(read_only=True)
    date = serializers.DateTimeField()
    user = serializers.CharField(max_length=255)
    groupname = serializers.CharField(max_length=255)
    pulse = serializers.FloatField()
    bps = serializers.CharField(max_length=40)
    bpd = serializers.CharField(max_length=40)
    weight = serializers.FloatField()
    height = serializers.FloatField()
    bmi = serializers.FloatField()
    waist_circ = serializers.FloatField()
    activity = serializers.FloatField()
    temperature = serializers.FloatField()
    glucose = serializers.FloatField()

    class Meta:
        model = FormVitals


class FormReviewofsSerializer(serializers.Serializer):
    #id = serializers.PrimaryKeyRelatedField(read_only=True)
    date = serializers.DateTimeField()
    dry_mouth = serializers.CharField(max_length=5)
    high_blood_pressure = serializers.CharField(max_length=5)
    user = serializers.CharField(max_length=255)
    groupname = serializers.CharField(max_length=255)

    class Meta:
        model = FormReviewofs


# Forms, List, HistoryData, PatientData
##################################################
class FormsSerializer(NonNullSerializer):
    #id = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField()
    encounter = serializers.IntegerField()
    form_name = serializers.CharField()
    user = serializers.CharField(max_length=255)
    deleted = serializers.IntegerField(default=0)

    # Inherited
    form_encounter = FormEncounterSerializer()
    form_ros = FormRosSerializer()
    form_vitals = FormVitalsSerializer()
    form_reviewofs = FormReviewofsSerializer()

    class Meta:
        model = Forms
        exclude = ('med_his', 'form_id', 'id')


class HistoryDataSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    tobacco = serializers.CharField()
    relatives_diabetes = serializers.CharField()
    relatives_high_blood_pressure = serializers.CharField()

    class Meta:
        model = HistoryData


class ListsSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    type = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)

    class Meta:
        model = Lists
        exclude = ('med_his',)


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
        exclude = ('street', 'ss', 'pid',)


# MedicalHistory
###########################################################
class ListMedicalHistorySerializer(serializers.Serializer):
    history_data = serializers.SerializerMethodField(method_name='hsearch_by_pid') # HistoryDataSerializer(many=True)
    #forms = serializers.SerializerMethodField(method_name='fsearch_by_pid') # FormsSerializer(many=True)
    #lists = serializers.SerializerMethodField(method_name='lsearch_by_pid') # ListsSerializer(many=True)

    class Meta:
        model = MedicalHistory

    def hsearch_by_pid(self, instance):
        visit = HistoryData.objects.filter(pid=instance.pid).latest('date')
        serializer = HistoryDataSerializer(instance=visit)
        return serializer.data

    def fsearch_by_pid(self, instance):
        visit = Forms.objects.filter(pid=instance.pid)
        serializer = FormsSerializer(instance=visit, many=True)
        return serializer.data

    def lsearch_by_pid(self, instance):
        visit = Lists.objects.filter(pid=instance.pid)
        serializer = ListsSerializer(instance=visit, many=True)
        return serializer.data


class CreateUpdateMedicalHistorySerializer(serializers.ModelSerializer):
    patient_data = PatientDataSerializer()
    history_data = HistoryDataSerializer(many=True)
    forms = FormsSerializer(many=True)
    lists = ListsSerializer(many=True)

    class Meta:
        model = MedicalHistory
        exclude = ('pid',)
