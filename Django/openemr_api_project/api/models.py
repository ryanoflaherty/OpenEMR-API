from __future__ import unicode_literals
from django.db import models

# Create your models here.
class HistoryData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    coffee = models.TextField(blank=True, null=True)
    tobacco = models.TextField(blank=True, null=True)
    alcohol = models.TextField(blank=True, null=True)
    sleep_patterns = models.TextField(blank=True, null=True)
    exercise_patterns = models.TextField(blank=True, null=True)
    seatbelt_use = models.TextField(blank=True, null=True)
    counseling = models.TextField(blank=True, null=True)
    hazardous_activities = models.TextField(blank=True, null=True)
    recreational_drugs = models.TextField(blank=True, null=True)
    last_breast_exam = models.CharField(max_length=255, blank=True, null=True)
    last_mammogram = models.CharField(max_length=255, blank=True, null=True)
    last_gynocological_exam = models.CharField(max_length=255, blank=True, null=True)
    last_rectal_exam = models.CharField(max_length=255, blank=True, null=True)
    last_prostate_exam = models.CharField(max_length=255, blank=True, null=True)
    last_physical_exam = models.CharField(max_length=255, blank=True, null=True)
    last_sigmoidoscopy_colonoscopy = models.CharField(max_length=255, blank=True, null=True)
    last_ecg = models.CharField(max_length=255, blank=True, null=True)
    last_cardiac_echo = models.CharField(max_length=255, blank=True, null=True)
    last_retinal = models.CharField(max_length=255, blank=True, null=True)
    last_fluvax = models.CharField(max_length=255, blank=True, null=True)
    last_pneuvax = models.CharField(max_length=255, blank=True, null=True)
    last_ldl = models.CharField(max_length=255, blank=True, null=True)
    last_hemoglobin = models.CharField(max_length=255, blank=True, null=True)
    last_psa = models.CharField(max_length=255, blank=True, null=True)
    last_exam_results = models.CharField(max_length=255, blank=True, null=True)
    history_mother = models.TextField(blank=True, null=True)
    dc_mother = models.TextField(blank=True, null=True)
    history_father = models.TextField(blank=True, null=True)
    dc_father = models.TextField(blank=True, null=True)
    history_siblings = models.TextField(blank=True, null=True)
    dc_siblings = models.TextField(blank=True, null=True)
    history_offspring = models.TextField(blank=True, null=True)
    dc_offspring = models.TextField(blank=True, null=True)
    history_spouse = models.TextField(blank=True, null=True)
    dc_spouse = models.TextField(blank=True, null=True)
    relatives_cancer = models.TextField(blank=True, null=True)
    relatives_tuberculosis = models.TextField(blank=True, null=True)
    relatives_diabetes = models.TextField(blank=True, null=True)
    relatives_high_blood_pressure = models.TextField(blank=True, null=True)
    relatives_heart_problems = models.TextField(blank=True, null=True)
    relatives_stroke = models.TextField(blank=True, null=True)
    relatives_epilepsy = models.TextField(blank=True, null=True)
    relatives_mental_illness = models.TextField(blank=True, null=True)
    relatives_suicide = models.TextField(blank=True, null=True)
    cataract_surgery = models.DateTimeField(blank=True, null=True)
    tonsillectomy = models.DateTimeField(blank=True, null=True)
    cholecystestomy = models.DateTimeField(blank=True, null=True)
    heart_surgery = models.DateTimeField(blank=True, null=True)
    hysterectomy = models.DateTimeField(blank=True, null=True)
    hernia_repair = models.DateTimeField(blank=True, null=True)
    hip_replacement = models.DateTimeField(blank=True, null=True)
    knee_replacement = models.DateTimeField(blank=True, null=True)
    appendectomy = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField()
    name_1 = models.CharField(max_length=255, blank=True, null=True)
    value_1 = models.CharField(max_length=255, blank=True, null=True)
    name_2 = models.CharField(max_length=255, blank=True, null=True)
    value_2 = models.CharField(max_length=255, blank=True, null=True)
    additional_history = models.TextField(blank=True, null=True)
    exams = models.TextField()
    usertext11 = models.TextField()
    usertext12 = models.CharField(max_length=255)
    usertext13 = models.CharField(max_length=255)
    usertext14 = models.CharField(max_length=255)
    usertext15 = models.CharField(max_length=255)
    usertext16 = models.CharField(max_length=255)
    usertext17 = models.CharField(max_length=255)
    usertext18 = models.CharField(max_length=255)
    usertext19 = models.CharField(max_length=255)
    usertext20 = models.CharField(max_length=255)
    usertext21 = models.CharField(max_length=255)
    usertext22 = models.CharField(max_length=255)
    usertext23 = models.CharField(max_length=255)
    usertext24 = models.CharField(max_length=255)
    usertext25 = models.CharField(max_length=255)
    usertext26 = models.CharField(max_length=255)
    usertext27 = models.CharField(max_length=255)
    usertext28 = models.CharField(max_length=255)
    usertext29 = models.CharField(max_length=255)
    usertext30 = models.CharField(max_length=255)
    userdate11 = models.DateField(blank=True, null=True)
    userdate12 = models.DateField(blank=True, null=True)
    userdate13 = models.DateField(blank=True, null=True)
    userdate14 = models.DateField(blank=True, null=True)
    userdate15 = models.DateField(blank=True, null=True)
    userarea11 = models.TextField()
    userarea12 = models.TextField()

    def __unicode__(self):
        return str(self.pid)

    class Meta:
        managed = False
        db_table = 'history_data'


class InsuranceData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=9, blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    plan_name = models.CharField(max_length=255, blank=True, null=True)
    policy_number = models.CharField(max_length=255, blank=True, null=True)
    group_number = models.CharField(max_length=255, blank=True, null=True)
    subscriber_lname = models.CharField(max_length=255, blank=True, null=True)
    subscriber_mname = models.CharField(max_length=255, blank=True, null=True)
    subscriber_fname = models.CharField(max_length=255, blank=True, null=True)
    subscriber_relationship = models.CharField(max_length=255, blank=True, null=True)
    subscriber_ss = models.CharField(max_length=255, blank=True, null=True)
    subscriber_dob = models.DateField(db_column='subscriber_DOB', blank=True, null=True)  # Field name made lowercase.
    subscriber_street = models.CharField(max_length=255, blank=True, null=True)
    subscriber_postal_code = models.CharField(max_length=255, blank=True, null=True)
    subscriber_city = models.CharField(max_length=255, blank=True, null=True)
    subscriber_state = models.CharField(max_length=255, blank=True, null=True)
    subscriber_country = models.CharField(max_length=255, blank=True, null=True)
    subscriber_phone = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer_street = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer_postal_code = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer_state = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer_country = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer_city = models.CharField(max_length=255, blank=True, null=True)
    copay = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    pid = models.BigIntegerField()
    subscriber_sex = models.CharField(max_length=25, blank=True, null=True)
    accept_assignment = models.CharField(max_length=5)
    policy_type = models.CharField(max_length=25)

    def __unicode__(self):
        return str(self.pid) + ', ' + self.type

    class Meta:
        managed = False
        db_table = 'insurance_data'
        unique_together = (('pid', 'type', 'date'),)

class PatientData(models.Model):
    id = models.BigIntegerField(primary_key=True)
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

    def __unicode__(self):
         return str(self.pid) + ', ' + self.lname

    class Meta:
        managed = False
        db_table = 'patient_data'

class FormEncounter(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    facility = models.TextField(blank=True, null=True)
    facility_id = models.IntegerField()
    pid = models.BigIntegerField(blank=True, null=True)
    encounter = models.BigIntegerField(blank=True, null=True)
    onset_date = models.DateTimeField(blank=True, null=True)
    sensitivity = models.CharField(max_length=30, blank=True, null=True)
    billing_note = models.TextField(blank=True, null=True)
    pc_catid = models.IntegerField()
    last_level_billed = models.IntegerField()
    last_level_closed = models.IntegerField()
    last_stmt_date = models.DateField(blank=True, null=True)
    stmt_count = models.IntegerField()
    provider_id = models.IntegerField(blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    invoice_refno = models.CharField(max_length=31)
    referral_source = models.CharField(max_length=31)
    billing_facility = models.IntegerField()

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
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()
    formdir = models.TextField(blank=True, null=True)

    def __unicode__(self):
         return str(self.pid) + ', ' + str(self.encounter) + ', ' + self.form_name

    class Meta:
        managed = False
        db_table = 'forms'

class Lists(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    begdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    returndate = models.DateField(blank=True, null=True)
    occurrence = models.IntegerField(blank=True, null=True)
    classification = models.IntegerField(blank=True, null=True)
    referredby = models.CharField(max_length=255, blank=True, null=True)
    extrainfo = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    outcome = models.IntegerField()
    destination = models.CharField(max_length=255, blank=True, null=True)
    reinjury_id = models.BigIntegerField()
    injury_part = models.CharField(max_length=31)
    injury_type = models.CharField(max_length=31)
    injury_grade = models.CharField(max_length=31)
    reaction = models.CharField(max_length=255)
    external_allergyid = models.IntegerField(blank=True, null=True)
    erx_source = models.CharField(max_length=1)
    erx_uploaded = models.CharField(max_length=1)
    modifydate = models.DateTimeField()

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

