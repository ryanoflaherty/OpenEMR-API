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
    lat = models.FloatField(verbose_name='Latitude', blank=True, null=True)
    long = models.FloatField(verbose_name='Longitude', blank=True, null=True)

    class Meta:
        managed = True


"""
This class will be used primarily for search functionality, as well as holding information that will typically not
change for each patient once they are created.
"""


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    med_his = models.ForeignKey('MedicalHistory', related_name='foreign')

    class Meta:
        managed = True


class PatientData(models.Model):
    pid = models.BigIntegerField(unique=True, primary_key=True)
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
    med_his = models.OneToOneField('MedicalHistory', default=1, related_name='patient_data')

    def __unicode__(self):
         return str(self.pid) + ', ' + self.lname

    class Meta:
        managed = False
        db_table = 'patient_data'

"""
This is the original PatientData class.  We might need to use it in the even that we need python to migrate our new
columns and indexes over

class PatientData(models.Model):
    id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    financial = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    drivers_license = models.CharField(max_length=255)
    ss = models.CharField(max_length=255)
    occupation = models.TextField(blank=True, null=True)
    phone_home = models.CharField(max_length=255)
    phone_biz = models.CharField(max_length=255)
    phone_contact = models.CharField(max_length=255)
    phone_cell = models.CharField(max_length=255)
    pharmacy_id = models.IntegerField()
    status = models.CharField(max_length=255)
    contact_relationship = models.CharField(max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    sex = models.CharField(max_length=255)
    referrer = models.CharField(max_length=255)
    referrerid = models.CharField(db_column='referrerID', max_length=255)  # Field name made lowercase.
    providerid = models.IntegerField(db_column='providerID', blank=True, null=True)  # Field name made lowercase.
    ref_providerid = models.IntegerField(db_column='ref_providerID', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    email_direct = models.CharField(max_length=255)
    ethnoracial = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    interpretter = models.CharField(max_length=255)
    migrantseasonal = models.CharField(max_length=255)
    family_size = models.CharField(max_length=255)
    monthly_income = models.CharField(max_length=255)
    homeless = models.CharField(max_length=255)
    financial_review = models.DateTimeField(blank=True, null=True)
    pubpid = models.CharField(max_length=255)
    pid = models.BigIntegerField(unique=True)
    genericname1 = models.CharField(max_length=255)
    genericval1 = models.CharField(max_length=255)
    genericname2 = models.CharField(max_length=255)
    genericval2 = models.CharField(max_length=255)
    hipaa_mail = models.CharField(max_length=3)
    hipaa_voice = models.CharField(max_length=3)
    hipaa_notice = models.CharField(max_length=3)
    hipaa_message = models.CharField(max_length=20)
    hipaa_allowsms = models.CharField(max_length=3)
    hipaa_allowemail = models.CharField(max_length=3)
    squad = models.CharField(max_length=32)
    fitness = models.IntegerField()
    referral_source = models.CharField(max_length=30)
    usertext1 = models.CharField(max_length=255)
    usertext2 = models.CharField(max_length=255)
    usertext3 = models.CharField(max_length=255)
    usertext4 = models.CharField(max_length=255)
    usertext5 = models.CharField(max_length=255)
    usertext6 = models.CharField(max_length=255)
    usertext7 = models.CharField(max_length=255)
    usertext8 = models.CharField(max_length=255)
    userlist1 = models.CharField(max_length=255)
    userlist2 = models.CharField(max_length=255)
    userlist3 = models.CharField(max_length=255)
    userlist4 = models.CharField(max_length=255)
    userlist5 = models.CharField(max_length=255)
    userlist6 = models.CharField(max_length=255)
    userlist7 = models.CharField(max_length=255)
    pricelevel = models.CharField(max_length=255)
    regdate = models.DateField(blank=True, null=True)
    contrastart = models.DateField(blank=True, null=True)
    completed_ad = models.CharField(max_length=3)
    ad_reviewed = models.DateField(blank=True, null=True)
    vfc = models.CharField(max_length=255)
    mothersname = models.CharField(max_length=255)
    guardiansname = models.CharField(max_length=255)
    allow_imm_reg_use = models.CharField(max_length=255)
    allow_imm_info_share = models.CharField(max_length=255)
    allow_health_info_ex = models.CharField(max_length=255)
    allow_patient_portal = models.CharField(max_length=31)
    deceased_date = models.DateTimeField(blank=True, null=True)
    deceased_reason = models.CharField(max_length=255)
    soap_import_status = models.IntegerField(blank=True, null=True)
    cmsportal_login = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'patient_data'
"""

"""
These classes are used to store data from a patients visit, including vitals, location, and family history
"""


class HistoryData(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(null=False)
    tobacco = models.TextField(blank=True, null=True)
    relatives_diabetes = models.TextField(blank=True, null=True)
    relatives_high_blood_pressure = models.TextField(blank=True, null=True)
    med_his = models.ForeignKey(MedicalHistory, default=3, related_name='history_data')

    def __unicode__(self):
        return '%d: %s' % (self.pid, self.date)

    class Meta:
        managed = False
        db_table = 'history_data'
        ordering = ['date']

class FormEncounter(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    facility = models.TextField(blank=True, null=True)
    facility_id = models.IntegerField()
    encounter = models.BigIntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
         return str(self.pid) + ', ' + str(self.encounter)

    class Meta:
        managed = False
        db_table = 'form_encounter'

class IssueEncounter(models.Model):
    # (ming) set primary_key to pid instead of the default autoincremented id
    pid = models.IntegerField(primary_key=True)
    list_id = models.IntegerField()
    encounter = models.IntegerField()
    resolved = models.IntegerField()

    def __unicode__(self):
        return str(self.pid) + ', ' + str(self.encounter) + ', ' + str(self.list_id)

    class Meta:
        managed = False
        db_table = 'issue_encounter'
        unique_together = (('pid', 'list_id', 'encounter'),)
        
class Forms(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    encounter = models.BigIntegerField(blank=True, null=True)
    form_name = models.TextField(blank=True, null=True)
    form_id = models.BigIntegerField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    def __unicode__(self):
         return str(self.pid) + ', ' + str(self.encounter) + ', ' + self.form_name

    class Meta:
        managed = False
        db_table = 'forms'

class Lists(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    begdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)

    def __unicode__(self):
         return str(self.pid) + ', ' + self.user + ', ' + self.type

    class Meta:
        managed = False
        db_table = 'lists'

class ListsTouch(models.Model):
    # (ming) set primary_key to pid instead of the default autoincremented id
   pid = models.BigIntegerField(primary_key=True)
   type = models.CharField(max_length=255)
   date = models.DateTimeField(blank=True, null=True)

   def __unicode__(self):
       return str(self.pid) + ', ' + self.type

   class Meta:
       managed = False
       db_table = 'lists_touch'
       unique_together = (('pid', 'type'),)

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

class FormVitals(models.Model):
    id = models.BigIntegerField(primary_key=True)
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

    def __unicode__(self):
       return str(self.pid)

    class Meta:
        managed = False
        db_table = 'form_vitals'

class FormReviewofs(models.Model):
    id = models.BigIntegerField(primary_key=True)
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
