from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.

# TODO (Ryan 3/14) - Add in the additional fields for blood sugar into OpenEMR via admin GUI
# http://htmlpreview.github.io/?https://github.com/fndtn357/openemr/blob/master/assets/openemrER.html

"""
Store a list of all medical objects associated with a patient data object
"""


class MedicalHistory(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.BigIntegerField(unique=True)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        managed = True


class PatientData(models.Model):
    pid = models.OneToOneField(MedicalHistory, db_column='pid', to_field='pid', related_name='patient_data', primary_key=True, unique=True)
    pubpid = models.CharField(max_length=255)
    ss = models.CharField(max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, null=True)
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=255)
    status = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255)
    street = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    country_code = models.CharField(max_length=255, null=True)
    phone_contact = models.CharField(max_length=255, null=True)
    phone_cell = models.CharField(max_length=255, null=True)

    def __unicode__(self):
         return str(self.pid) + ', ' + self.lname

    class Meta:
        managed = False
        db_table = 'patient_data'


class HistoryData(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(null=False)
    tobacco = models.TextField(blank=True, null=True)
    relatives_diabetes = models.TextField(blank=True, null=True)
    relatives_high_blood_pressure = models.TextField(blank=True, null=True)
    med_his = models.ForeignKey(MedicalHistory, related_name='history_data')

    def __unicode__(self):
        return '%d: %s' % (self.pid, self.date)

    class Meta:
        managed = False
        db_table = 'history_data'
        ordering = ['date']


class Forms(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    encounter = models.BigIntegerField(unique=True, blank=True, null=True)
    form_name = models.TextField(blank=True, null=True)
    form_id = models.BigIntegerField(blank=True, null=True, unique=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(null=False, default=0)
    med_his = models.ForeignKey(MedicalHistory, related_name='forms')

    def __unicode__(self):
         return str(self.pid) + ', ' + str(self.encounter) + ', ' + self.form_name

    class Meta:
        managed = False
        db_table = 'forms'
        ordering = ['encounter']


class Lists(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    med_his = models.ForeignKey(MedicalHistory, related_name='lists')

    def __unicode__(self):
         return str(self.pid) + ', ' + self.user + ', ' + self.type

    class Meta:
        managed = False
        db_table = 'lists'


class IssueEncounter(models.Model):
    # (ming) set primary_key to pid instead of the default autoincremented id
    pid = models.IntegerField(primary_key=True, null=False)
    list_id = models.IntegerField(null=False)
    encounter = models.IntegerField(null=False)
    resolved = models.IntegerField(null=False)

    def __unicode__(self):
        return str(self.pid) + ', ' + str(self.encounter) + ', ' + str(self.list_id)

    class Meta:
        managed = False
        db_table = 'issue_encounter'
        unique_together = (('pid', 'list_id', 'encounter'),)


class Facility(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    facility_npi = models.CharField(max_length=15, blank=True, null=True)
    service_location = models.IntegerField()
    billing_location = models.IntegerField()
    color = models.CharField(max_length=7)

    def __unicode__(self):
       return str(self.id) + ', ' + self.name

    class Meta:
        managed = False
        db_table = 'facility'


class FormEncounter(models.Model):
    id = models.OneToOneField(Forms, db_column='id', to_field='form_id', related_name='form_encounter', primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    facility_id = models.ForeignKey(Facility, db_column='facility_id', related_name='facility')
    encounter = models.BigIntegerField(unique=True)

    def __unicode__(self):
         return str(self.pid) + ', ' + str(self.encounter)

    class Meta:
        managed = False
        db_table = 'form_encounter'


class FormVitals(models.Model):
    id = models.OneToOneField(Forms, db_column='id', to_field='form_id', related_name='form_vitals', primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    pulse = models.FloatField(blank=True, null=True)
    bps = models.CharField(max_length=40, blank=True, null=True)
    bpd = models.CharField(max_length=40, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(db_column='BMI', blank=True, null=True)  # Field name made lowercase.
    waist_circ = models.FloatField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    glucose = models.FloatField(blank=True, null=True)

    def __unicode__(self):
       return str(self.pid)

    class Meta:
        managed = False
        db_table = 'form_vitals'


class FormReviewofs(models.Model):
    id = models.OneToOneField(Forms, db_column='id', to_field='form_id', related_name='form_reviewofs', primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    dry_mouth = models.CharField(max_length=5, blank=True, null=True)
    high_blood_pressure = models.CharField(max_length=5, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
       return str(self.pid) + ', ' + str(self.date)

    class Meta:
        managed = False
        db_table = 'form_reviewofs'


class FormRos(models.Model):
    id = models.OneToOneField(Forms, db_column='id', to_field='form_id', related_name='form_ros', primary_key=True)
    pid = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    p = models.CharField(max_length=3, blank=True, null=True)
    n_numbness = models.CharField(max_length=3, blank=True, null=True)
    n_weakness = models.CharField(max_length=3, blank=True, null=True)
    diabetes = models.CharField(max_length=3, blank=True, null=True)

    def __unicode__(self):
       return str(self.pid) + ', ' + str(self.date)

    class Meta:
        managed = False
        db_table = 'form_ros'


class Visit(models.Model):
    id = models.AutoField(primary_key=True)
    encounter = models.OneToOneField(FormEncounter, db_column='encounter', to_field='encounter', related_name='fk_encounter')
    #form_id = models.ForeignKey(Forms, to_field='form_id', related_name='fk_form_id')
    form_reviewofs = models.ForeignKey(FormReviewofs, related_name='fk_form_reviewofs')
    form_vitals = models.ForeignKey(FormVitals, related_name='fk_form_vitals')
    form_ros = models.ForeignKey(FormRos, related_name='fk_form_ros')
    med_his = models.ForeignKey(MedicalHistory, related_name='visits')

    def __unicode__(self):
        return str(self.encounter)

    class Meta:
        managed = True