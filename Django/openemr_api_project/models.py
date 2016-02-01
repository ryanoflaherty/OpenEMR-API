# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Addresses(models.Model):
    id = models.IntegerField(primary_key=True)
    line1 = models.CharField(max_length=255, blank=True, null=True)
    line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=35, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    plus_four = models.CharField(max_length=4, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    foreign_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class AmcMiscData(models.Model):
    amc_id = models.CharField(max_length=31)
    pid = models.BigIntegerField(blank=True, null=True)
    map_category = models.CharField(max_length=255)
    map_id = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amc_misc_data'


class Amendments(models.Model):
    amendment_id = models.AutoField(primary_key=True)
    amendment_date = models.DateField()
    amendment_by = models.CharField(max_length=50)
    amendment_status = models.CharField(max_length=50, blank=True, null=True)
    pid = models.IntegerField()
    amendment_desc = models.TextField()
    created_by = models.IntegerField()
    modified_by = models.IntegerField(blank=True, null=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amendments'


class AmendmentsHistory(models.Model):
    amendment_id = models.AutoField()
    amendment_note = models.TextField()
    amendment_status = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'amendments_history'


class ArActivity(models.Model):
    pid = models.IntegerField()
    encounter = models.IntegerField()
    sequence_no = models.AutoField()
    code_type = models.CharField(max_length=12)
    code = models.CharField(max_length=20)
    modifier = models.CharField(max_length=12)
    payer_type = models.IntegerField()
    post_time = models.DateTimeField()
    post_user = models.IntegerField()
    session_id = models.IntegerField()
    memo = models.CharField(max_length=255)
    pay_amount = models.DecimalField(max_digits=12, decimal_places=2)
    adj_amount = models.DecimalField(max_digits=12, decimal_places=2)
    modified_time = models.DateTimeField()
    follow_up = models.CharField(max_length=1)
    follow_up_note = models.TextField()
    account_code = models.CharField(max_length=15)
    reason_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_activity'
        unique_together = (('pid', 'encounter', 'sequence_no'),)


class ArSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    payer_id = models.IntegerField()
    user_id = models.IntegerField()
    closed = models.IntegerField()
    reference = models.CharField(max_length=255)
    check_date = models.DateField(blank=True, null=True)
    deposit_date = models.DateField(blank=True, null=True)
    pay_total = models.DecimalField(max_digits=12, decimal_places=2)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    global_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=50)
    description = models.TextField()
    adjustment_code = models.CharField(max_length=50)
    post_to_date = models.DateField()
    patient_id = models.IntegerField()
    payment_method = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'ar_session'


class Array(models.Model):
    array_key = models.CharField(max_length=255, blank=True, null=True)
    array_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'array'


class AuditDetails(models.Model):
    id = models.BigIntegerField(primary_key=True)
    table_name = models.CharField(max_length=100)
    field_name = models.CharField(max_length=100)
    field_value = models.TextField()
    audit_master_id = models.BigIntegerField()
    entry_identification = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'audit_details'


class AuditMaster(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField()
    user_id = models.BigIntegerField()
    approval_status = models.IntegerField()
    comments = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    ip_address = models.CharField(max_length=100)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audit_master'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AutomaticNotification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    sms_gateway_type = models.CharField(max_length=255)
    next_app_date = models.DateField()
    next_app_time = models.CharField(max_length=10)
    provider_name = models.CharField(max_length=100)
    message = models.TextField()
    email_sender = models.CharField(max_length=100)
    email_subject = models.CharField(max_length=100)
    type = models.CharField(max_length=5)
    notification_sent_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'automatic_notification'


class BackgroundServices(models.Model):
    name = models.CharField(primary_key=True, max_length=31)
    title = models.CharField(max_length=127)
    active = models.IntegerField()
    running = models.IntegerField()
    next_run = models.DateTimeField()
    execute_interval = models.IntegerField()
    function = models.CharField(max_length=127)
    require_once = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'background_services'


class Batchcom(models.Model):
    id = models.BigIntegerField(primary_key=True)
    patient_id = models.IntegerField()
    sent_by = models.BigIntegerField()
    msg_type = models.CharField(max_length=60, blank=True, null=True)
    msg_subject = models.CharField(max_length=255, blank=True, null=True)
    msg_text = models.TextField(blank=True, null=True)
    msg_date_sent = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'batchcom'


class Billing(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    code_type = models.CharField(max_length=15, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    encounter = models.IntegerField(blank=True, null=True)
    code_text = models.TextField(blank=True, null=True)
    billed = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    payer_id = models.IntegerField(blank=True, null=True)
    bill_process = models.IntegerField()
    bill_date = models.DateTimeField(blank=True, null=True)
    process_date = models.DateTimeField(blank=True, null=True)
    process_file = models.CharField(max_length=255, blank=True, null=True)
    modifier = models.CharField(max_length=12, blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)
    fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    justify = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=30, blank=True, null=True)
    x12_partner_id = models.IntegerField(blank=True, null=True)
    ndc_info = models.CharField(max_length=255, blank=True, null=True)
    notecodes = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'billing'


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    parent = models.IntegerField()
    lft = models.IntegerField()
    rght = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categories'


class CategoriesSeq(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'categories_seq'


class CategoriesToDocuments(models.Model):
    category_id = models.IntegerField()
    document_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categories_to_documents'
        unique_together = (('category_id', 'document_id'),)


class ChartTracker(models.Model):
    ct_pid = models.IntegerField()
    ct_when = models.DateTimeField()
    ct_userid = models.BigIntegerField()
    ct_location = models.CharField(max_length=31)

    class Meta:
        managed = False
        db_table = 'chart_tracker'
        unique_together = (('ct_pid', 'ct_when'),)


class Claims(models.Model):
    patient_id = models.IntegerField()
    encounter_id = models.IntegerField()
    version = models.AutoField()
    payer_id = models.IntegerField()
    status = models.IntegerField()
    payer_type = models.IntegerField()
    bill_process = models.IntegerField()
    bill_time = models.DateTimeField(blank=True, null=True)
    process_time = models.DateTimeField(blank=True, null=True)
    process_file = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=30, blank=True, null=True)
    x12_partner_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'claims'
        unique_together = (('patient_id', 'encounter_id', 'version'),)


class ClinicalPlans(models.Model):
    id = models.CharField(max_length=31)
    pid = models.BigIntegerField()
    normal_flag = models.IntegerField(blank=True, null=True)
    cqm_flag = models.IntegerField(blank=True, null=True)
    cqm_2011_flag = models.IntegerField(blank=True, null=True)
    cqm_2014_flag = models.IntegerField(blank=True, null=True)
    cqm_measure_group = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'clinical_plans'
        unique_together = (('id', 'pid'),)


class ClinicalPlansRules(models.Model):
    plan_id = models.CharField(max_length=31)
    rule_id = models.CharField(max_length=31)

    class Meta:
        managed = False
        db_table = 'clinical_plans_rules'
        unique_together = (('plan_id', 'rule_id'),)


class ClinicalRules(models.Model):
    id = models.CharField(max_length=31)
    pid = models.BigIntegerField()
    active_alert_flag = models.IntegerField(blank=True, null=True)
    passive_alert_flag = models.IntegerField(blank=True, null=True)
    cqm_flag = models.IntegerField(blank=True, null=True)
    cqm_2011_flag = models.IntegerField(blank=True, null=True)
    cqm_2014_flag = models.IntegerField(blank=True, null=True)
    cqm_nqf_code = models.CharField(max_length=10)
    cqm_pqri_code = models.CharField(max_length=10)
    amc_flag = models.IntegerField(blank=True, null=True)
    amc_2011_flag = models.IntegerField(blank=True, null=True)
    amc_2014_flag = models.IntegerField(blank=True, null=True)
    amc_code = models.CharField(max_length=10)
    amc_code_2014 = models.CharField(max_length=30)
    patient_reminder_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_rules'
        unique_together = (('id', 'pid'),)


class CodeTypes(models.Model):
    ct_key = models.CharField(primary_key=True, max_length=15)
    ct_id = models.IntegerField(unique=True)
    ct_seq = models.IntegerField()
    ct_mod = models.IntegerField()
    ct_just = models.CharField(max_length=15)
    ct_mask = models.CharField(max_length=9)
    ct_fee = models.IntegerField()
    ct_rel = models.IntegerField()
    ct_nofs = models.IntegerField()
    ct_diag = models.IntegerField()
    ct_active = models.IntegerField()
    ct_label = models.CharField(max_length=31)
    ct_external = models.IntegerField()
    ct_claim = models.IntegerField()
    ct_proc = models.IntegerField()
    ct_term = models.IntegerField()
    ct_problem = models.IntegerField()
    ct_drug = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'code_types'


class Codes(models.Model):
    code_text = models.CharField(max_length=255)
    code_text_short = models.CharField(max_length=24)
    code = models.CharField(max_length=25)
    code_type = models.SmallIntegerField(blank=True, null=True)
    modifier = models.CharField(max_length=12)
    units = models.IntegerField(blank=True, null=True)
    fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    superbill = models.CharField(max_length=31)
    related_code = models.CharField(max_length=255)
    taxrates = models.CharField(max_length=255)
    cyp_factor = models.FloatField()
    active = models.IntegerField(blank=True, null=True)
    reportable = models.IntegerField(blank=True, null=True)
    financial_reporting = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codes'


class Config(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    parent = models.IntegerField()
    lft = models.IntegerField()
    rght = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'config'


class ConfigSeq(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'config_seq'


class Customlists(models.Model):
    cl_list_slno = models.AutoField(primary_key=True)
    cl_list_id = models.IntegerField()
    cl_list_item_id = models.IntegerField(blank=True, null=True)
    cl_list_type = models.IntegerField()
    cl_list_item_short = models.CharField(max_length=10, blank=True, null=True)
    cl_list_item_long = models.TextField()
    cl_list_item_level = models.IntegerField(blank=True, null=True)
    cl_order = models.IntegerField(blank=True, null=True)
    cl_deleted = models.IntegerField(blank=True, null=True)
    cl_creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customlists'


class DatedReminders(models.Model):
    dr_id = models.AutoField(primary_key=True)
    dr_from_id = models.IntegerField(db_column='dr_from_ID')  # Field name made lowercase.
    dr_message_text = models.CharField(max_length=160)
    dr_message_sent_date = models.DateTimeField()
    dr_message_due_date = models.DateField()
    pid = models.IntegerField()
    message_priority = models.IntegerField()
    message_processed = models.IntegerField()
    processed_date = models.DateTimeField(blank=True, null=True)
    dr_processed_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dated_reminders'


class DatedRemindersLink(models.Model):
    dr_link_id = models.AutoField(primary_key=True)
    dr_id = models.IntegerField()
    to_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dated_reminders_link'


class DirectMessageLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    msg_type = models.CharField(max_length=1)
    msg_id = models.CharField(max_length=127)
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    create_ts = models.DateTimeField()
    status = models.CharField(max_length=1)
    status_info = models.CharField(max_length=511, blank=True, null=True)
    status_ts = models.DateTimeField(blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direct_message_log'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documents(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=8, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)
    revision = models.DateTimeField()
    foreign_id = models.IntegerField(blank=True, null=True)
    docdate = models.DateField(blank=True, null=True)
    hash = models.CharField(max_length=40, blank=True, null=True)
    list_id = models.BigIntegerField()
    couch_docid = models.CharField(max_length=100, blank=True, null=True)
    couch_revid = models.CharField(max_length=100, blank=True, null=True)
    storagemethod = models.IntegerField()
    path_depth = models.IntegerField(blank=True, null=True)
    imported = models.IntegerField(blank=True, null=True)
    encounter_id = models.BigIntegerField()
    encounter_check = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'documents'


class DocumentsLegalCategories(models.Model):
    dlc_id = models.AutoField(primary_key=True)
    dlc_category_type = models.IntegerField()
    dlc_category_name = models.CharField(max_length=45)
    dlc_category_parent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_legal_categories'


class DocumentsLegalDetail(models.Model):
    dld_id = models.AutoField(primary_key=True)
    dld_pid = models.IntegerField(blank=True, null=True)
    dld_facility = models.IntegerField(blank=True, null=True)
    dld_provider = models.IntegerField(blank=True, null=True)
    dld_encounter = models.IntegerField(blank=True, null=True)
    dld_master_docid = models.IntegerField()
    dld_signed = models.SmallIntegerField()
    dld_signed_time = models.DateTimeField()
    dld_filepath = models.CharField(max_length=75, blank=True, null=True)
    dld_filename = models.CharField(max_length=45)
    dld_signing_person = models.CharField(max_length=50)
    dld_sign_level = models.IntegerField()
    dld_content = models.CharField(max_length=50)
    dld_file_for_pdf_generation = models.TextField()
    dld_denial_reason = models.TextField()
    dld_moved = models.IntegerField()
    dld_patient_comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_legal_detail'


class DocumentsLegalMaster(models.Model):
    dlm_category = models.IntegerField(blank=True, null=True)
    dlm_subcategory = models.IntegerField(blank=True, null=True)
    dlm_document_id = models.AutoField(primary_key=True)
    dlm_document_name = models.CharField(max_length=75)
    dlm_filepath = models.CharField(max_length=75)
    dlm_facility = models.IntegerField(blank=True, null=True)
    dlm_provider = models.IntegerField(blank=True, null=True)
    dlm_sign_height = models.FloatField()
    dlm_sign_width = models.FloatField()
    dlm_filename = models.CharField(max_length=45)
    dlm_effective_date = models.DateTimeField()
    dlm_version = models.IntegerField()
    content = models.CharField(max_length=255)
    dlm_savedsign = models.CharField(max_length=255, blank=True, null=True)
    dlm_review = models.CharField(max_length=255, blank=True, null=True)
    dlm_upload_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_legal_master'


class DrugInventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    drug_id = models.IntegerField()
    lot_number = models.CharField(max_length=20, blank=True, null=True)
    expiration = models.DateField(blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    on_hand = models.IntegerField()
    warehouse_id = models.CharField(max_length=31)
    vendor_id = models.BigIntegerField()
    last_notify = models.DateField()
    destroy_date = models.DateField(blank=True, null=True)
    destroy_method = models.CharField(max_length=255, blank=True, null=True)
    destroy_witness = models.CharField(max_length=255, blank=True, null=True)
    destroy_notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_inventory'


class DrugSales(models.Model):
    sale_id = models.AutoField(primary_key=True)
    drug_id = models.IntegerField()
    inventory_id = models.IntegerField()
    prescription_id = models.IntegerField()
    pid = models.IntegerField()
    encounter = models.IntegerField()
    user = models.CharField(max_length=255, blank=True, null=True)
    sale_date = models.DateField()
    quantity = models.IntegerField()
    fee = models.DecimalField(max_digits=12, decimal_places=2)
    billed = models.IntegerField()
    xfer_inventory_id = models.IntegerField()
    distributor_id = models.BigIntegerField()
    notes = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'drug_sales'


class DrugTemplates(models.Model):
    drug_id = models.IntegerField()
    selector = models.CharField(max_length=255)
    dosage = models.CharField(max_length=10, blank=True, null=True)
    period = models.IntegerField()
    quantity = models.IntegerField()
    refills = models.IntegerField()
    taxrates = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_templates'
        unique_together = (('drug_id', 'selector'),)


class Drugs(models.Model):
    drug_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ndc_number = models.CharField(max_length=20)
    on_order = models.IntegerField()
    reorder_point = models.FloatField()
    max_level = models.FloatField()
    last_notify = models.DateField()
    reactions = models.TextField(blank=True, null=True)
    form = models.IntegerField()
    size = models.FloatField()
    unit = models.IntegerField()
    route = models.IntegerField()
    substitute = models.IntegerField()
    related_code = models.CharField(max_length=255)
    cyp_factor = models.FloatField()
    active = models.IntegerField(blank=True, null=True)
    allow_combining = models.IntegerField()
    allow_multiple = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drugs'


class EligibilityResponse(models.Model):
    response_id = models.BigIntegerField(primary_key=True)
    response_description = models.CharField(max_length=255, blank=True, null=True)
    response_status = models.CharField(max_length=1)
    response_vendor_id = models.BigIntegerField(blank=True, null=True)
    response_create_date = models.DateField(blank=True, null=True)
    response_modify_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eligibility_response'


class EligibilityVerification(models.Model):
    verification_id = models.BigIntegerField(primary_key=True)
    response_id = models.BigIntegerField(blank=True, null=True)
    insurance_id = models.BigIntegerField(blank=True, null=True)
    eligibility_check_date = models.DateTimeField(blank=True, null=True)
    copay = models.IntegerField(blank=True, null=True)
    deductible = models.IntegerField(blank=True, null=True)
    deductiblemet = models.CharField(max_length=1, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eligibility_verification'


class EmployerData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'employer_data'


class EncCategoryMap(models.Model):
    rule_enc_id = models.CharField(max_length=31)
    main_cat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'enc_category_map'


class ErxTtlTouch(models.Model):
    patient_id = models.BigIntegerField()
    process = models.CharField(max_length=11)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'erx_ttl_touch'
        unique_together = (('patient_id', 'process'),)


class EsignSignatures(models.Model):
    tid = models.IntegerField()
    table = models.CharField(max_length=255)
    uid = models.IntegerField()
    datetime = models.DateTimeField()
    is_lock = models.IntegerField()
    amendment = models.TextField(blank=True, null=True)
    hash = models.CharField(max_length=255)
    signature_hash = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'esign_signatures'


class ExtendedLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    recipient = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extended_log'


class Facility(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=11, blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    federal_ein = models.CharField(max_length=15, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    service_location = models.IntegerField()
    billing_location = models.IntegerField()
    accepts_assignment = models.IntegerField()
    pos_code = models.IntegerField(blank=True, null=True)
    x12_sender_id = models.CharField(max_length=25, blank=True, null=True)
    attn = models.CharField(max_length=65, blank=True, null=True)
    domain_identifier = models.CharField(max_length=60, blank=True, null=True)
    facility_npi = models.CharField(max_length=15, blank=True, null=True)
    tax_id_type = models.CharField(max_length=31)
    color = models.CharField(max_length=7)
    primary_business_entity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'facility'


class FacilityUserIds(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uid = models.BigIntegerField(blank=True, null=True)
    facility_id = models.BigIntegerField(blank=True, null=True)
    field_id = models.CharField(max_length=31)
    field_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'facility_user_ids'


class FeeSheetOptions(models.Model):
    fs_category = models.CharField(max_length=63, blank=True, null=True)
    fs_option = models.CharField(max_length=63, blank=True, null=True)
    fs_codes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fee_sheet_options'


class FormDictation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    dictation = models.TextField(blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_dictation'


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

    class Meta:
        managed = False
        db_table = 'form_encounter'


class FormMiscBillingOptions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    employment_related = models.IntegerField(blank=True, null=True)
    auto_accident = models.IntegerField(blank=True, null=True)
    accident_state = models.CharField(max_length=2, blank=True, null=True)
    other_accident = models.IntegerField(blank=True, null=True)
    outside_lab = models.IntegerField(blank=True, null=True)
    lab_amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    is_unable_to_work = models.IntegerField(blank=True, null=True)
    date_initial_treatment = models.DateField(blank=True, null=True)
    off_work_from = models.DateField(blank=True, null=True)
    off_work_to = models.DateField(blank=True, null=True)
    is_hospitalized = models.IntegerField(blank=True, null=True)
    hospitalization_date_from = models.DateField(blank=True, null=True)
    hospitalization_date_to = models.DateField(blank=True, null=True)
    medicaid_resubmission_code = models.CharField(max_length=10, blank=True, null=True)
    medicaid_original_reference = models.CharField(max_length=15, blank=True, null=True)
    prior_auth_number = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    replacement_claim = models.IntegerField(blank=True, null=True)
    box_14_date_qual = models.CharField(max_length=3, blank=True, null=True)
    box_15_date_qual = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_misc_billing_options'


class FormReviewofs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    fever = models.CharField(max_length=5, blank=True, null=True)
    chills = models.CharField(max_length=5, blank=True, null=True)
    night_sweats = models.CharField(max_length=5, blank=True, null=True)
    weight_loss = models.CharField(max_length=5, blank=True, null=True)
    poor_appetite = models.CharField(max_length=5, blank=True, null=True)
    insomnia = models.CharField(max_length=5, blank=True, null=True)
    fatigued = models.CharField(max_length=5, blank=True, null=True)
    depressed = models.CharField(max_length=5, blank=True, null=True)
    hyperactive = models.CharField(max_length=5, blank=True, null=True)
    exposure_to_foreign_countries = models.CharField(max_length=5, blank=True, null=True)
    cataracts = models.CharField(max_length=5, blank=True, null=True)
    cataract_surgery = models.CharField(max_length=5, blank=True, null=True)
    glaucoma = models.CharField(max_length=5, blank=True, null=True)
    double_vision = models.CharField(max_length=5, blank=True, null=True)
    blurred_vision = models.CharField(max_length=5, blank=True, null=True)
    poor_hearing = models.CharField(max_length=5, blank=True, null=True)
    headaches = models.CharField(max_length=5, blank=True, null=True)
    ringing_in_ears = models.CharField(max_length=5, blank=True, null=True)
    bloody_nose = models.CharField(max_length=5, blank=True, null=True)
    sinusitis = models.CharField(max_length=5, blank=True, null=True)
    sinus_surgery = models.CharField(max_length=5, blank=True, null=True)
    dry_mouth = models.CharField(max_length=5, blank=True, null=True)
    strep_throat = models.CharField(max_length=5, blank=True, null=True)
    tonsillectomy = models.CharField(max_length=5, blank=True, null=True)
    swollen_lymph_nodes = models.CharField(max_length=5, blank=True, null=True)
    throat_cancer = models.CharField(max_length=5, blank=True, null=True)
    throat_cancer_surgery = models.CharField(max_length=5, blank=True, null=True)
    heart_attack = models.CharField(max_length=5, blank=True, null=True)
    irregular_heart_beat = models.CharField(max_length=5, blank=True, null=True)
    chest_pains = models.CharField(max_length=5, blank=True, null=True)
    shortness_of_breath = models.CharField(max_length=5, blank=True, null=True)
    high_blood_pressure = models.CharField(max_length=5, blank=True, null=True)
    heart_failure = models.CharField(max_length=5, blank=True, null=True)
    poor_circulation = models.CharField(max_length=5, blank=True, null=True)
    vascular_surgery = models.CharField(max_length=5, blank=True, null=True)
    cardiac_catheterization = models.CharField(max_length=5, blank=True, null=True)
    coronary_artery_bypass = models.CharField(max_length=5, blank=True, null=True)
    heart_transplant = models.CharField(max_length=5, blank=True, null=True)
    stress_test = models.CharField(max_length=5, blank=True, null=True)
    emphysema = models.CharField(max_length=5, blank=True, null=True)
    chronic_bronchitis = models.CharField(max_length=5, blank=True, null=True)
    interstitial_lung_disease = models.CharField(max_length=5, blank=True, null=True)
    shortness_of_breath_2 = models.CharField(max_length=5, blank=True, null=True)
    lung_cancer = models.CharField(max_length=5, blank=True, null=True)
    lung_cancer_surgery = models.CharField(max_length=5, blank=True, null=True)
    pheumothorax = models.CharField(max_length=5, blank=True, null=True)
    stomach_pains = models.CharField(max_length=5, blank=True, null=True)
    peptic_ulcer_disease = models.CharField(max_length=5, blank=True, null=True)
    gastritis = models.CharField(max_length=5, blank=True, null=True)
    endoscopy = models.CharField(max_length=5, blank=True, null=True)
    polyps = models.CharField(max_length=5, blank=True, null=True)
    colonoscopy = models.CharField(max_length=5, blank=True, null=True)
    colon_cancer = models.CharField(max_length=5, blank=True, null=True)
    colon_cancer_surgery = models.CharField(max_length=5, blank=True, null=True)
    ulcerative_colitis = models.CharField(max_length=5, blank=True, null=True)
    crohns_disease = models.CharField(max_length=5, blank=True, null=True)
    appendectomy = models.CharField(max_length=5, blank=True, null=True)
    divirticulitis = models.CharField(max_length=5, blank=True, null=True)
    divirticulitis_surgery = models.CharField(max_length=5, blank=True, null=True)
    gall_stones = models.CharField(max_length=5, blank=True, null=True)
    cholecystectomy = models.CharField(max_length=5, blank=True, null=True)
    hepatitis = models.CharField(max_length=5, blank=True, null=True)
    cirrhosis_of_the_liver = models.CharField(max_length=5, blank=True, null=True)
    splenectomy = models.CharField(max_length=5, blank=True, null=True)
    kidney_failure = models.CharField(max_length=5, blank=True, null=True)
    kidney_stones = models.CharField(max_length=5, blank=True, null=True)
    kidney_cancer = models.CharField(max_length=5, blank=True, null=True)
    kidney_infections = models.CharField(max_length=5, blank=True, null=True)
    bladder_infections = models.CharField(max_length=5, blank=True, null=True)
    bladder_cancer = models.CharField(max_length=5, blank=True, null=True)
    prostate_problems = models.CharField(max_length=5, blank=True, null=True)
    prostate_cancer = models.CharField(max_length=5, blank=True, null=True)
    kidney_transplant = models.CharField(max_length=5, blank=True, null=True)
    sexually_transmitted_disease = models.CharField(max_length=5, blank=True, null=True)
    burning_with_urination = models.CharField(max_length=5, blank=True, null=True)
    discharge_from_urethra = models.CharField(max_length=5, blank=True, null=True)
    rashes = models.CharField(max_length=5, blank=True, null=True)
    infections = models.CharField(max_length=5, blank=True, null=True)
    ulcerations = models.CharField(max_length=5, blank=True, null=True)
    pemphigus = models.CharField(max_length=5, blank=True, null=True)
    herpes = models.CharField(max_length=5, blank=True, null=True)
    osetoarthritis = models.CharField(max_length=5, blank=True, null=True)
    rheumotoid_arthritis = models.CharField(max_length=5, blank=True, null=True)
    lupus = models.CharField(max_length=5, blank=True, null=True)
    ankylosing_sondlilitis = models.CharField(max_length=5, blank=True, null=True)
    swollen_joints = models.CharField(max_length=5, blank=True, null=True)
    stiff_joints = models.CharField(max_length=5, blank=True, null=True)
    broken_bones = models.CharField(max_length=5, blank=True, null=True)
    neck_problems = models.CharField(max_length=5, blank=True, null=True)
    back_problems = models.CharField(max_length=5, blank=True, null=True)
    back_surgery = models.CharField(max_length=5, blank=True, null=True)
    scoliosis = models.CharField(max_length=5, blank=True, null=True)
    herniated_disc = models.CharField(max_length=5, blank=True, null=True)
    shoulder_problems = models.CharField(max_length=5, blank=True, null=True)
    elbow_problems = models.CharField(max_length=5, blank=True, null=True)
    wrist_problems = models.CharField(max_length=5, blank=True, null=True)
    hand_problems = models.CharField(max_length=5, blank=True, null=True)
    hip_problems = models.CharField(max_length=5, blank=True, null=True)
    knee_problems = models.CharField(max_length=5, blank=True, null=True)
    ankle_problems = models.CharField(max_length=5, blank=True, null=True)
    foot_problems = models.CharField(max_length=5, blank=True, null=True)
    insulin_dependent_diabetes = models.CharField(max_length=5, blank=True, null=True)
    noninsulin_dependent_diabetes = models.CharField(max_length=5, blank=True, null=True)
    hypothyroidism = models.CharField(max_length=5, blank=True, null=True)
    hyperthyroidism = models.CharField(max_length=5, blank=True, null=True)
    cushing_syndrom = models.CharField(max_length=5, blank=True, null=True)
    addison_syndrom = models.CharField(max_length=5, blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_reviewofs'


class FormRos(models.Model):
    pid = models.IntegerField()
    activity = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    weight_change = models.CharField(max_length=3, blank=True, null=True)
    weakness = models.CharField(max_length=3, blank=True, null=True)
    fatigue = models.CharField(max_length=3, blank=True, null=True)
    anorexia = models.CharField(max_length=3, blank=True, null=True)
    fever = models.CharField(max_length=3, blank=True, null=True)
    chills = models.CharField(max_length=3, blank=True, null=True)
    night_sweats = models.CharField(max_length=3, blank=True, null=True)
    insomnia = models.CharField(max_length=3, blank=True, null=True)
    irritability = models.CharField(max_length=3, blank=True, null=True)
    heat_or_cold = models.CharField(max_length=3, blank=True, null=True)
    intolerance = models.CharField(max_length=3, blank=True, null=True)
    change_in_vision = models.CharField(max_length=3, blank=True, null=True)
    glaucoma_history = models.CharField(max_length=3, blank=True, null=True)
    eye_pain = models.CharField(max_length=3, blank=True, null=True)
    irritation = models.CharField(max_length=3, blank=True, null=True)
    redness = models.CharField(max_length=3, blank=True, null=True)
    excessive_tearing = models.CharField(max_length=3, blank=True, null=True)
    double_vision = models.CharField(max_length=3, blank=True, null=True)
    blind_spots = models.CharField(max_length=3, blank=True, null=True)
    photophobia = models.CharField(max_length=3, blank=True, null=True)
    hearing_loss = models.CharField(max_length=3, blank=True, null=True)
    discharge = models.CharField(max_length=3, blank=True, null=True)
    pain = models.CharField(max_length=3, blank=True, null=True)
    vertigo = models.CharField(max_length=3, blank=True, null=True)
    tinnitus = models.CharField(max_length=3, blank=True, null=True)
    frequent_colds = models.CharField(max_length=3, blank=True, null=True)
    sore_throat = models.CharField(max_length=3, blank=True, null=True)
    sinus_problems = models.CharField(max_length=3, blank=True, null=True)
    post_nasal_drip = models.CharField(max_length=3, blank=True, null=True)
    nosebleed = models.CharField(max_length=3, blank=True, null=True)
    snoring = models.CharField(max_length=3, blank=True, null=True)
    apnea = models.CharField(max_length=3, blank=True, null=True)
    breast_mass = models.CharField(max_length=3, blank=True, null=True)
    breast_discharge = models.CharField(max_length=3, blank=True, null=True)
    biopsy = models.CharField(max_length=3, blank=True, null=True)
    abnormal_mammogram = models.CharField(max_length=3, blank=True, null=True)
    cough = models.CharField(max_length=3, blank=True, null=True)
    sputum = models.CharField(max_length=3, blank=True, null=True)
    shortness_of_breath = models.CharField(max_length=3, blank=True, null=True)
    wheezing = models.CharField(max_length=3, blank=True, null=True)
    hemoptsyis = models.CharField(max_length=3, blank=True, null=True)
    asthma = models.CharField(max_length=3, blank=True, null=True)
    copd = models.CharField(max_length=3, blank=True, null=True)
    chest_pain = models.CharField(max_length=3, blank=True, null=True)
    palpitation = models.CharField(max_length=3, blank=True, null=True)
    syncope = models.CharField(max_length=3, blank=True, null=True)
    pnd = models.CharField(max_length=3, blank=True, null=True)
    doe = models.CharField(max_length=3, blank=True, null=True)
    orthopnea = models.CharField(max_length=3, blank=True, null=True)
    peripheal = models.CharField(max_length=3, blank=True, null=True)
    edema = models.CharField(max_length=3, blank=True, null=True)
    legpain_cramping = models.CharField(max_length=3, blank=True, null=True)
    history_murmur = models.CharField(max_length=3, blank=True, null=True)
    arrythmia = models.CharField(max_length=3, blank=True, null=True)
    heart_problem = models.CharField(max_length=3, blank=True, null=True)
    dysphagia = models.CharField(max_length=3, blank=True, null=True)
    heartburn = models.CharField(max_length=3, blank=True, null=True)
    bloating = models.CharField(max_length=3, blank=True, null=True)
    belching = models.CharField(max_length=3, blank=True, null=True)
    flatulence = models.CharField(max_length=3, blank=True, null=True)
    nausea = models.CharField(max_length=3, blank=True, null=True)
    vomiting = models.CharField(max_length=3, blank=True, null=True)
    hematemesis = models.CharField(max_length=3, blank=True, null=True)
    gastro_pain = models.CharField(max_length=3, blank=True, null=True)
    food_intolerance = models.CharField(max_length=3, blank=True, null=True)
    hepatitis = models.CharField(max_length=3, blank=True, null=True)
    jaundice = models.CharField(max_length=3, blank=True, null=True)
    hematochezia = models.CharField(max_length=3, blank=True, null=True)
    changed_bowel = models.CharField(max_length=3, blank=True, null=True)
    diarrhea = models.CharField(max_length=3, blank=True, null=True)
    constipation = models.CharField(max_length=3, blank=True, null=True)
    polyuria = models.CharField(max_length=3, blank=True, null=True)
    polydypsia = models.CharField(max_length=3, blank=True, null=True)
    dysuria = models.CharField(max_length=3, blank=True, null=True)
    hematuria = models.CharField(max_length=3, blank=True, null=True)
    frequency = models.CharField(max_length=3, blank=True, null=True)
    urgency = models.CharField(max_length=3, blank=True, null=True)
    incontinence = models.CharField(max_length=3, blank=True, null=True)
    renal_stones = models.CharField(max_length=3, blank=True, null=True)
    utis = models.CharField(max_length=3, blank=True, null=True)
    hesitancy = models.CharField(max_length=3, blank=True, null=True)
    dribbling = models.CharField(max_length=3, blank=True, null=True)
    stream = models.CharField(max_length=3, blank=True, null=True)
    nocturia = models.CharField(max_length=3, blank=True, null=True)
    erections = models.CharField(max_length=3, blank=True, null=True)
    ejaculations = models.CharField(max_length=3, blank=True, null=True)
    g = models.CharField(max_length=3, blank=True, null=True)
    p = models.CharField(max_length=3, blank=True, null=True)
    ap = models.CharField(max_length=3, blank=True, null=True)
    lc = models.CharField(max_length=3, blank=True, null=True)
    mearche = models.CharField(max_length=3, blank=True, null=True)
    menopause = models.CharField(max_length=3, blank=True, null=True)
    lmp = models.CharField(max_length=3, blank=True, null=True)
    f_frequency = models.CharField(max_length=3, blank=True, null=True)
    f_flow = models.CharField(max_length=3, blank=True, null=True)
    f_symptoms = models.CharField(max_length=3, blank=True, null=True)
    abnormal_hair_growth = models.CharField(max_length=3, blank=True, null=True)
    f_hirsutism = models.CharField(max_length=3, blank=True, null=True)
    joint_pain = models.CharField(max_length=3, blank=True, null=True)
    swelling = models.CharField(max_length=3, blank=True, null=True)
    m_redness = models.CharField(max_length=3, blank=True, null=True)
    m_warm = models.CharField(max_length=3, blank=True, null=True)
    m_stiffness = models.CharField(max_length=3, blank=True, null=True)
    muscle = models.CharField(max_length=3, blank=True, null=True)
    m_aches = models.CharField(max_length=3, blank=True, null=True)
    fms = models.CharField(max_length=3, blank=True, null=True)
    arthritis = models.CharField(max_length=3, blank=True, null=True)
    loc = models.CharField(max_length=3, blank=True, null=True)
    seizures = models.CharField(max_length=3, blank=True, null=True)
    stroke = models.CharField(max_length=3, blank=True, null=True)
    tia = models.CharField(max_length=3, blank=True, null=True)
    n_numbness = models.CharField(max_length=3, blank=True, null=True)
    n_weakness = models.CharField(max_length=3, blank=True, null=True)
    paralysis = models.CharField(max_length=3, blank=True, null=True)
    intellectual_decline = models.CharField(max_length=3, blank=True, null=True)
    memory_problems = models.CharField(max_length=3, blank=True, null=True)
    dementia = models.CharField(max_length=3, blank=True, null=True)
    n_headache = models.CharField(max_length=3, blank=True, null=True)
    s_cancer = models.CharField(max_length=3, blank=True, null=True)
    psoriasis = models.CharField(max_length=3, blank=True, null=True)
    s_acne = models.CharField(max_length=3, blank=True, null=True)
    s_other = models.CharField(max_length=3, blank=True, null=True)
    s_disease = models.CharField(max_length=3, blank=True, null=True)
    p_diagnosis = models.CharField(max_length=3, blank=True, null=True)
    p_medication = models.CharField(max_length=3, blank=True, null=True)
    depression = models.CharField(max_length=3, blank=True, null=True)
    anxiety = models.CharField(max_length=3, blank=True, null=True)
    social_difficulties = models.CharField(max_length=3, blank=True, null=True)
    thyroid_problems = models.CharField(max_length=3, blank=True, null=True)
    diabetes = models.CharField(max_length=3, blank=True, null=True)
    abnormal_blood = models.CharField(max_length=3, blank=True, null=True)
    anemia = models.CharField(max_length=3, blank=True, null=True)
    fh_blood_problems = models.CharField(max_length=3, blank=True, null=True)
    bleeding_problems = models.CharField(max_length=3, blank=True, null=True)
    allergies = models.CharField(max_length=3, blank=True, null=True)
    frequent_illness = models.CharField(max_length=3, blank=True, null=True)
    hiv = models.CharField(max_length=3, blank=True, null=True)
    hai_status = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_ros'


class FormSoap(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    subjective = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    assessment = models.TextField(blank=True, null=True)
    plan = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_soap'


class FormVitals(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    bps = models.CharField(max_length=40, blank=True, null=True)
    bpd = models.CharField(max_length=40, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    temp_method = models.CharField(max_length=255, blank=True, null=True)
    pulse = models.FloatField(blank=True, null=True)
    respiration = models.FloatField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    bmi = models.FloatField(db_column='BMI', blank=True, null=True)  # Field name made lowercase.
    bmi_status = models.CharField(db_column='BMI_status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    waist_circ = models.FloatField(blank=True, null=True)
    head_circ = models.FloatField(blank=True, null=True)
    oxygen_saturation = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_vitals'


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

    class Meta:
        managed = False
        db_table = 'forms'


class GaclAcl(models.Model):
    id = models.IntegerField(primary_key=True)
    section_value = models.CharField(max_length=150)
    allow = models.IntegerField()
    enabled = models.IntegerField()
    return_value = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    updated_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_acl'


class GaclAclSections(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(unique=True, max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=230)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_acl_sections'


class GaclAclSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_acl_seq'


class GaclAco(models.Model):
    id = models.IntegerField(primary_key=True)
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=255)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aco'
        unique_together = (('section_value', 'value'),)


class GaclAcoMap(models.Model):
    acl_id = models.IntegerField()
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_aco_map'
        unique_together = (('acl_id', 'section_value', 'value'),)


class GaclAcoSections(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(unique=True, max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=230)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aco_sections'


class GaclAcoSectionsSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aco_sections_seq'


class GaclAcoSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aco_seq'


class GaclAro(models.Model):
    id = models.IntegerField(primary_key=True)
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=255)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro'
        unique_together = (('section_value', 'value'),)


class GaclAroGroups(models.Model):
    id = models.IntegerField()
    parent_id = models.IntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_aro_groups'
        unique_together = (('id', 'value'),)


class GaclAroGroupsIdSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro_groups_id_seq'


class GaclAroGroupsMap(models.Model):
    acl_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro_groups_map'
        unique_together = (('acl_id', 'group_id'),)


class GaclAroMap(models.Model):
    acl_id = models.IntegerField()
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_aro_map'
        unique_together = (('acl_id', 'section_value', 'value'),)


class GaclAroSections(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(unique=True, max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=230)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro_sections'


class GaclAroSectionsSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro_sections_seq'


class GaclAroSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro_seq'


class GaclAxo(models.Model):
    id = models.IntegerField(primary_key=True)
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=255)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_axo'
        unique_together = (('section_value', 'value'),)


class GaclAxoGroups(models.Model):
    id = models.IntegerField()
    parent_id = models.IntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_axo_groups'
        unique_together = (('id', 'value'),)


class GaclAxoGroupsMap(models.Model):
    acl_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_axo_groups_map'
        unique_together = (('acl_id', 'group_id'),)


class GaclAxoMap(models.Model):
    acl_id = models.IntegerField()
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_axo_map'
        unique_together = (('acl_id', 'section_value', 'value'),)


class GaclAxoSections(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(unique=True, max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=230)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_axo_sections'


class GaclGroupsAroMap(models.Model):
    group_id = models.IntegerField()
    aro_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_groups_aro_map'
        unique_together = (('group_id', 'aro_id'),)


class GaclGroupsAxoMap(models.Model):
    group_id = models.IntegerField()
    axo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_groups_axo_map'
        unique_together = (('group_id', 'axo_id'),)


class GaclPhpgacl(models.Model):
    name = models.CharField(primary_key=True, max_length=230)
    value = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_phpgacl'


class GeoCountryReference(models.Model):
    countries_id = models.AutoField(primary_key=True)
    countries_name = models.CharField(max_length=64, blank=True, null=True)
    countries_iso_code_2 = models.CharField(max_length=2)
    countries_iso_code_3 = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'geo_country_reference'


class GeoZoneReference(models.Model):
    zone_id = models.AutoField(primary_key=True)
    zone_country_id = models.IntegerField()
    zone_code = models.CharField(max_length=5, blank=True, null=True)
    zone_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_zone_reference'


class Globals(models.Model):
    gl_name = models.CharField(max_length=63)
    gl_index = models.IntegerField()
    gl_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'globals'
        unique_together = (('gl_name', 'gl_index'),)


class Gprelations(models.Model):
    type1 = models.IntegerField()
    id1 = models.BigIntegerField()
    type2 = models.IntegerField()
    id2 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'gprelations'
        unique_together = (('type1', 'id1', 'type2', 'id2'),)


class Groups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    user = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


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

    class Meta:
        managed = False
        db_table = 'history_data'


class Icd10DxOrderCode(models.Model):
    dx_id = models.BigIntegerField(unique=True)
    dx_code = models.CharField(max_length=7, blank=True, null=True)
    formatted_dx_code = models.CharField(max_length=10, blank=True, null=True)
    valid_for_coding = models.CharField(max_length=1, blank=True, null=True)
    short_desc = models.CharField(max_length=60, blank=True, null=True)
    long_desc = models.CharField(max_length=300, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_dx_order_code'


class Icd10GemDx109(models.Model):
    map_id = models.BigIntegerField(unique=True)
    dx_icd10_source = models.CharField(max_length=7, blank=True, null=True)
    dx_icd9_target = models.CharField(max_length=5, blank=True, null=True)
    flags = models.CharField(max_length=5, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_gem_dx_10_9'


class Icd10GemDx910(models.Model):
    map_id = models.BigIntegerField(unique=True)
    dx_icd9_source = models.CharField(max_length=5, blank=True, null=True)
    dx_icd10_target = models.CharField(max_length=7, blank=True, null=True)
    flags = models.CharField(max_length=5, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_gem_dx_9_10'


class Icd10GemPcs109(models.Model):
    map_id = models.BigIntegerField(unique=True)
    pcs_icd10_source = models.CharField(max_length=7, blank=True, null=True)
    pcs_icd9_target = models.CharField(max_length=5, blank=True, null=True)
    flags = models.CharField(max_length=5, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_gem_pcs_10_9'


class Icd10GemPcs910(models.Model):
    map_id = models.BigIntegerField(unique=True)
    pcs_icd9_source = models.CharField(max_length=5, blank=True, null=True)
    pcs_icd10_target = models.CharField(max_length=7, blank=True, null=True)
    flags = models.CharField(max_length=5, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_gem_pcs_9_10'


class Icd10PcsOrderCode(models.Model):
    pcs_id = models.BigIntegerField(unique=True)
    pcs_code = models.CharField(max_length=7, blank=True, null=True)
    valid_for_coding = models.CharField(max_length=1, blank=True, null=True)
    short_desc = models.CharField(max_length=60, blank=True, null=True)
    long_desc = models.CharField(max_length=300, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_pcs_order_code'


class Icd10ReimbrDx910(models.Model):
    map_id = models.BigIntegerField(unique=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    code_cnt = models.IntegerField(blank=True, null=True)
    icd9_01 = models.CharField(db_column='ICD9_01', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_02 = models.CharField(db_column='ICD9_02', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_03 = models.CharField(db_column='ICD9_03', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_04 = models.CharField(db_column='ICD9_04', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_05 = models.CharField(db_column='ICD9_05', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_06 = models.CharField(db_column='ICD9_06', max_length=5, blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_reimbr_dx_9_10'


class Icd10ReimbrPcs910(models.Model):
    map_id = models.BigIntegerField(unique=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    code_cnt = models.IntegerField(blank=True, null=True)
    icd9_01 = models.CharField(db_column='ICD9_01', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_02 = models.CharField(db_column='ICD9_02', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_03 = models.CharField(db_column='ICD9_03', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_04 = models.CharField(db_column='ICD9_04', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_05 = models.CharField(db_column='ICD9_05', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_06 = models.CharField(db_column='ICD9_06', max_length=5, blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_reimbr_pcs_9_10'


class Icd9DxCode(models.Model):
    dx_id = models.BigIntegerField(unique=True)
    dx_code = models.CharField(max_length=5, blank=True, null=True)
    formatted_dx_code = models.CharField(max_length=6, blank=True, null=True)
    short_desc = models.CharField(max_length=60, blank=True, null=True)
    long_desc = models.CharField(max_length=300, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd9_dx_code'


class Icd9DxLongCode(models.Model):
    dx_id = models.BigIntegerField(unique=True)
    dx_code = models.CharField(max_length=5, blank=True, null=True)
    long_desc = models.CharField(max_length=300, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd9_dx_long_code'


class Icd9SgCode(models.Model):
    sg_id = models.BigIntegerField(unique=True)
    sg_code = models.CharField(max_length=5, blank=True, null=True)
    formatted_sg_code = models.CharField(max_length=6, blank=True, null=True)
    short_desc = models.CharField(max_length=60, blank=True, null=True)
    long_desc = models.CharField(max_length=300, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd9_sg_code'


class Icd9SgLongCode(models.Model):
    sq_id = models.BigIntegerField(unique=True)
    sg_code = models.CharField(max_length=5, blank=True, null=True)
    long_desc = models.CharField(max_length=300, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd9_sg_long_code'


class Immunizations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    patient_id = models.IntegerField(blank=True, null=True)
    administered_date = models.DateTimeField(blank=True, null=True)
    immunization_id = models.IntegerField(blank=True, null=True)
    cvx_code = models.IntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    lot_number = models.CharField(max_length=50, blank=True, null=True)
    administered_by_id = models.BigIntegerField(blank=True, null=True)
    administered_by = models.CharField(max_length=255, blank=True, null=True)
    education_date = models.DateField(blank=True, null=True)
    vis_date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    amount_administered = models.FloatField(blank=True, null=True)
    amount_administered_unit = models.CharField(max_length=50, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    route = models.CharField(max_length=100, blank=True, null=True)
    administration_site = models.CharField(max_length=100, blank=True, null=True)
    added_erroneously = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'immunizations'


class InsuranceCompanies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    attn = models.CharField(max_length=255, blank=True, null=True)
    cms_id = models.CharField(max_length=15, blank=True, null=True)
    freeb_type = models.IntegerField(blank=True, null=True)
    x12_receiver_id = models.CharField(max_length=25, blank=True, null=True)
    x12_default_partner_id = models.IntegerField(blank=True, null=True)
    alt_cms_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'insurance_companies'


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

    class Meta:
        managed = False
        db_table = 'insurance_data'
        unique_together = (('pid', 'type', 'date'),)


class InsuranceNumbers(models.Model):
    id = models.IntegerField(primary_key=True)
    provider_id = models.IntegerField()
    insurance_company_id = models.IntegerField(blank=True, null=True)
    provider_number = models.CharField(max_length=20, blank=True, null=True)
    rendering_provider_number = models.CharField(max_length=20, blank=True, null=True)
    group_number = models.CharField(max_length=20, blank=True, null=True)
    provider_number_type = models.CharField(max_length=4, blank=True, null=True)
    rendering_provider_number_type = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_numbers'


class IntegrationMapping(models.Model):
    id = models.IntegerField(primary_key=True)
    foreign_id = models.IntegerField()
    foreign_table = models.CharField(max_length=125, blank=True, null=True)
    local_id = models.IntegerField()
    local_table = models.CharField(max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'integration_mapping'
        unique_together = (('foreign_id', 'foreign_table', 'local_id', 'local_table'),)


class IssueEncounter(models.Model):
    pid = models.IntegerField()
    list_id = models.IntegerField()
    encounter = models.IntegerField()
    resolved = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'issue_encounter'
        unique_together = (('pid', 'list_id', 'encounter'),)


class IssueTypes(models.Model):
    active = models.IntegerField()
    category = models.CharField(max_length=75)
    type = models.CharField(max_length=75)
    plural = models.CharField(max_length=75)
    singular = models.CharField(max_length=75)
    abbreviation = models.CharField(max_length=75)
    style = models.SmallIntegerField()
    force_show = models.SmallIntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'issue_types'
        unique_together = (('category', 'type'),)


class LangConstants(models.Model):
    cons_id = models.AutoField(unique=True)
    constant_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lang_constants'


class LangCustom(models.Model):
    lang_description = models.CharField(max_length=100)
    lang_code = models.CharField(max_length=2)
    constant_name = models.CharField(max_length=255)
    definition = models.TextField()

    class Meta:
        managed = False
        db_table = 'lang_custom'


class LangDefinitions(models.Model):
    def_id = models.AutoField(unique=True)
    cons_id = models.IntegerField()
    lang_id = models.IntegerField()
    definition = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lang_definitions'


class LangLanguages(models.Model):
    lang_id = models.AutoField(unique=True)
    lang_code = models.CharField(max_length=2)
    lang_description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lang_languages'


class LayoutOptions(models.Model):
    form_id = models.CharField(max_length=31)
    field_id = models.CharField(max_length=31)
    group_name = models.CharField(max_length=31)
    title = models.CharField(max_length=63)
    seq = models.IntegerField()
    data_type = models.IntegerField()
    uor = models.IntegerField()
    fld_length = models.IntegerField()
    max_length = models.IntegerField()
    list_id = models.CharField(max_length=31)
    titlecols = models.IntegerField()
    datacols = models.IntegerField()
    default_value = models.CharField(max_length=255)
    edit_options = models.CharField(max_length=36)
    description = models.TextField(blank=True, null=True)
    fld_rows = models.IntegerField()
    list_backup_id = models.CharField(max_length=31)
    source = models.CharField(max_length=1)
    conditions = models.TextField()

    class Meta:
        managed = False
        db_table = 'layout_options'
        unique_together = (('form_id', 'field_id', 'seq'),)


class LbfData(models.Model):
    form_id = models.AutoField()
    field_id = models.CharField(max_length=31)
    field_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'lbf_data'
        unique_together = (('form_id', 'field_id'),)


class ListOptions(models.Model):
    list_id = models.CharField(max_length=31)
    option_id = models.CharField(max_length=31)
    title = models.CharField(max_length=255)
    seq = models.IntegerField()
    is_default = models.IntegerField()
    option_value = models.FloatField()
    mapping = models.CharField(max_length=31)
    notes = models.CharField(max_length=255)
    codes = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'list_options'
        unique_together = (('list_id', 'option_id'),)


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

    class Meta:
        managed = False
        db_table = 'lists'


class ListsTouch(models.Model):
    pid = models.BigIntegerField()
    type = models.CharField(max_length=255)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lists_touch'
        unique_together = (('pid', 'type'),)


class Log(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    user_notes = models.TextField(blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    checksum = models.TextField(blank=True, null=True)
    crt_user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class LogCommentEncrypt(models.Model):
    log_id = models.IntegerField()
    encrypt = models.CharField(max_length=3)
    checksum = models.TextField()

    class Meta:
        managed = False
        db_table = 'log_comment_encrypt'


class MiscAddressBook(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fname = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'misc_address_book'


class ModuleAclGroupSettings(models.Model):
    module_id = models.IntegerField()
    group_id = models.IntegerField()
    section_id = models.IntegerField()
    allowed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_acl_group_settings'
        unique_together = (('module_id', 'group_id', 'section_id'),)


class ModuleAclSections(models.Model):
    section_id = models.IntegerField(blank=True, null=True)
    section_name = models.CharField(max_length=255, blank=True, null=True)
    parent_section = models.IntegerField(blank=True, null=True)
    section_identifier = models.CharField(max_length=50, blank=True, null=True)
    module_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_acl_sections'


class ModuleAclUserSettings(models.Model):
    module_id = models.IntegerField()
    user_id = models.IntegerField()
    section_id = models.IntegerField()
    allowed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_acl_user_settings'
        unique_together = (('module_id', 'user_id', 'section_id'),)


class ModuleConfiguration(models.Model):
    module_config_id = models.AutoField(primary_key=True)
    module_id = models.IntegerField()
    field_name = models.CharField(max_length=45)
    field_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'module_configuration'


class Modules(models.Model):
    mod_id = models.AutoField()
    mod_name = models.CharField(max_length=64)
    mod_directory = models.CharField(max_length=64)
    mod_parent = models.CharField(max_length=64)
    mod_type = models.CharField(max_length=64)
    mod_active = models.IntegerField()
    mod_ui_name = models.CharField(max_length=20)
    mod_relative_link = models.CharField(max_length=64)
    mod_ui_order = models.IntegerField()
    mod_ui_active = models.IntegerField()
    mod_description = models.CharField(max_length=255)
    mod_nick_name = models.CharField(max_length=25)
    mod_enc_menu = models.CharField(max_length=10)
    permissions_item_table = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=255)
    date = models.DateTimeField()
    sql_run = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modules'
        unique_together = (('mod_id', 'mod_directory'),)


class ModulesHooksSettings(models.Model):
    mod_id = models.IntegerField(blank=True, null=True)
    enabled_hooks = models.CharField(max_length=255, blank=True, null=True)
    attached_to = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modules_hooks_settings'


class ModulesSettings(models.Model):
    mod_id = models.IntegerField(blank=True, null=True)
    fld_type = models.SmallIntegerField(blank=True, null=True)
    obj_name = models.CharField(max_length=255, blank=True, null=True)
    menu_name = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modules_settings'


class Notes(models.Model):
    id = models.IntegerField(primary_key=True)
    foreign_id = models.IntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    revision = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notes'


class NotificationLog(models.Model):
    ilogid = models.AutoField(db_column='iLogId', primary_key=True)  # Field name made lowercase.
    pid = models.IntegerField()
    pc_eid = models.IntegerField(blank=True, null=True)
    sms_gateway_type = models.CharField(max_length=50)
    smsgateway_info = models.CharField(max_length=255)
    message = models.TextField()
    email_sender = models.CharField(max_length=255)
    email_subject = models.CharField(max_length=255)
    type = models.CharField(max_length=5)
    patient_info = models.TextField()
    pc_eventdate = models.DateField(db_column='pc_eventDate')  # Field name made lowercase.
    pc_enddate = models.DateField(db_column='pc_endDate')  # Field name made lowercase.
    pc_starttime = models.TimeField(db_column='pc_startTime')  # Field name made lowercase.
    pc_endtime = models.TimeField(db_column='pc_endTime')  # Field name made lowercase.
    dsentdatetime = models.DateTimeField(db_column='dSentDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notification_log'


class NotificationSettings(models.Model):
    settingsid = models.AutoField(db_column='SettingsId', primary_key=True)  # Field name made lowercase.
    send_sms_before_hours = models.IntegerField(db_column='Send_SMS_Before_Hours')  # Field name made lowercase.
    send_email_before_hours = models.IntegerField(db_column='Send_Email_Before_Hours')  # Field name made lowercase.
    sms_gateway_username = models.CharField(db_column='SMS_gateway_username', max_length=100)  # Field name made lowercase.
    sms_gateway_password = models.CharField(db_column='SMS_gateway_password', max_length=100)  # Field name made lowercase.
    sms_gateway_apikey = models.CharField(db_column='SMS_gateway_apikey', max_length=100)  # Field name made lowercase.
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'notification_settings'


class Onotes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onotes'


class OpenemrModuleVars(models.Model):
    pn_id = models.AutoField(primary_key=True)
    pn_modname = models.CharField(max_length=64, blank=True, null=True)
    pn_name = models.CharField(max_length=64, blank=True, null=True)
    pn_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openemr_module_vars'


class OpenemrModules(models.Model):
    pn_id = models.AutoField(primary_key=True)
    pn_name = models.CharField(max_length=64, blank=True, null=True)
    pn_type = models.IntegerField()
    pn_displayname = models.CharField(max_length=64, blank=True, null=True)
    pn_description = models.CharField(max_length=255, blank=True, null=True)
    pn_regid = models.IntegerField()
    pn_directory = models.CharField(max_length=64, blank=True, null=True)
    pn_version = models.CharField(max_length=10, blank=True, null=True)
    pn_admin_capable = models.IntegerField()
    pn_user_capable = models.IntegerField()
    pn_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'openemr_modules'


class OpenemrPostcalendarCategories(models.Model):
    pc_catid = models.AutoField(primary_key=True)
    pc_catname = models.CharField(max_length=100, blank=True, null=True)
    pc_catcolor = models.CharField(max_length=50, blank=True, null=True)
    pc_catdesc = models.TextField(blank=True, null=True)
    pc_recurrtype = models.IntegerField()
    pc_enddate = models.DateField(blank=True, null=True)
    pc_recurrspec = models.TextField(blank=True, null=True)
    pc_recurrfreq = models.IntegerField()
    pc_duration = models.BigIntegerField()
    pc_end_date_flag = models.IntegerField()
    pc_end_date_type = models.IntegerField(blank=True, null=True)
    pc_end_date_freq = models.IntegerField()
    pc_end_all_day = models.IntegerField()
    pc_dailylimit = models.IntegerField()
    pc_cattype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'openemr_postcalendar_categories'


class OpenemrPostcalendarEvents(models.Model):
    pc_eid = models.AutoField(primary_key=True)
    pc_catid = models.IntegerField()
    pc_multiple = models.IntegerField()
    pc_aid = models.CharField(max_length=30, blank=True, null=True)
    pc_pid = models.CharField(max_length=11, blank=True, null=True)
    pc_title = models.CharField(max_length=150, blank=True, null=True)
    pc_time = models.DateTimeField(blank=True, null=True)
    pc_hometext = models.TextField(blank=True, null=True)
    pc_comments = models.IntegerField(blank=True, null=True)
    pc_counter = models.IntegerField(blank=True, null=True)
    pc_topic = models.IntegerField()
    pc_informant = models.CharField(max_length=20, blank=True, null=True)
    pc_eventdate = models.DateField(db_column='pc_eventDate')  # Field name made lowercase.
    pc_enddate = models.DateField(db_column='pc_endDate')  # Field name made lowercase.
    pc_duration = models.BigIntegerField()
    pc_recurrtype = models.IntegerField()
    pc_recurrspec = models.TextField(blank=True, null=True)
    pc_recurrfreq = models.IntegerField()
    pc_starttime = models.TimeField(db_column='pc_startTime', blank=True, null=True)  # Field name made lowercase.
    pc_endtime = models.TimeField(db_column='pc_endTime', blank=True, null=True)  # Field name made lowercase.
    pc_alldayevent = models.IntegerField()
    pc_location = models.TextField(blank=True, null=True)
    pc_conttel = models.CharField(max_length=50, blank=True, null=True)
    pc_contname = models.CharField(max_length=50, blank=True, null=True)
    pc_contemail = models.CharField(max_length=255, blank=True, null=True)
    pc_website = models.CharField(max_length=255, blank=True, null=True)
    pc_fee = models.CharField(max_length=50, blank=True, null=True)
    pc_eventstatus = models.IntegerField()
    pc_sharing = models.IntegerField()
    pc_language = models.CharField(max_length=30, blank=True, null=True)
    pc_apptstatus = models.CharField(max_length=15)
    pc_prefcatid = models.IntegerField()
    pc_facility = models.SmallIntegerField()
    pc_sendalertsms = models.CharField(max_length=3)
    pc_sendalertemail = models.CharField(max_length=3)
    pc_billing_location = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'openemr_postcalendar_events'


class OpenemrPostcalendarLimits(models.Model):
    pc_limitid = models.AutoField(primary_key=True)
    pc_catid = models.IntegerField()
    pc_starttime = models.TimeField()
    pc_endtime = models.TimeField()
    pc_limit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'openemr_postcalendar_limits'


class OpenemrPostcalendarTopics(models.Model):
    pc_catid = models.AutoField(primary_key=True)
    pc_catname = models.CharField(max_length=100, blank=True, null=True)
    pc_catcolor = models.CharField(max_length=50, blank=True, null=True)
    pc_catdesc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openemr_postcalendar_topics'


class OpenemrSessionInfo(models.Model):
    pn_sessid = models.CharField(primary_key=True, max_length=32)
    pn_ipaddr = models.CharField(max_length=20, blank=True, null=True)
    pn_firstused = models.IntegerField()
    pn_lastused = models.IntegerField()
    pn_uid = models.IntegerField()
    pn_vars = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openemr_session_info'


class PatientAccessOffsite(models.Model):
    pid = models.IntegerField(unique=True)
    portal_username = models.CharField(max_length=100)
    portal_pwd = models.CharField(max_length=100)
    portal_pwd_status = models.IntegerField(blank=True, null=True)
    authorize_net_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_access_offsite'


class PatientAccessOnsite(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    portal_username = models.CharField(max_length=100, blank=True, null=True)
    portal_pwd = models.CharField(max_length=100, blank=True, null=True)
    portal_pwd_status = models.IntegerField(blank=True, null=True)
    portal_salt = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_access_onsite'


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


class PatientReminders(models.Model):
    id = models.BigIntegerField(primary_key=True)
    active = models.IntegerField()
    date_inactivated = models.DateTimeField(blank=True, null=True)
    reason_inactivated = models.CharField(max_length=31)
    due_status = models.CharField(max_length=31)
    pid = models.BigIntegerField()
    category = models.CharField(max_length=31)
    item = models.CharField(max_length=31)
    date_created = models.DateTimeField(blank=True, null=True)
    date_sent = models.DateTimeField(blank=True, null=True)
    voice_status = models.IntegerField()
    sms_status = models.IntegerField()
    email_status = models.IntegerField()
    mail_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient_reminders'


class PaymentGatewayDetails(models.Model):
    service_name = models.CharField(max_length=100, blank=True, null=True)
    login_id = models.CharField(max_length=255, blank=True, null=True)
    transaction_key = models.CharField(max_length=255, blank=True, null=True)
    md5 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_details'


class Payments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField()
    dtime = models.DateTimeField()
    encounter = models.BigIntegerField()
    user = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    amount1 = models.DecimalField(max_digits=12, decimal_places=2)
    amount2 = models.DecimalField(max_digits=12, decimal_places=2)
    posted1 = models.DecimalField(max_digits=12, decimal_places=2)
    posted2 = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'payments'


class Pharmacies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    transmit_method = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmacies'


class PhoneNumbers(models.Model):
    id = models.IntegerField(primary_key=True)
    country_code = models.CharField(max_length=5, blank=True, null=True)
    area_code = models.CharField(max_length=3, blank=True, null=True)
    prefix = models.CharField(max_length=3, blank=True, null=True)
    number = models.CharField(max_length=4, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    foreign_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_numbers'


class PmaBookmark(models.Model):
    dbase = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    query = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pma_bookmark'


class PmaColumnInfo(models.Model):
    db_name = models.CharField(max_length=64, blank=True, null=True)
    table_name = models.CharField(max_length=64, blank=True, null=True)
    column_name = models.CharField(max_length=64, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255, blank=True, null=True)
    transformation = models.CharField(max_length=255, blank=True, null=True)
    transformation_options = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pma_column_info'
        unique_together = (('db_name', 'table_name', 'column_name'),)


class PmaHistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    db = models.CharField(max_length=64, blank=True, null=True)
    table = models.CharField(max_length=64, blank=True, null=True)
    timevalue = models.DateTimeField()
    sqlquery = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pma_history'


class PmaPdfPages(models.Model):
    db_name = models.CharField(max_length=64, blank=True, null=True)
    page_nr = models.AutoField(primary_key=True)
    page_descr = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pma_pdf_pages'


class PmaRelation(models.Model):
    master_db = models.CharField(max_length=64)
    master_table = models.CharField(max_length=64)
    master_field = models.CharField(max_length=64)
    foreign_db = models.CharField(max_length=64, blank=True, null=True)
    foreign_table = models.CharField(max_length=64, blank=True, null=True)
    foreign_field = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pma_relation'
        unique_together = (('master_db', 'master_table', 'master_field'),)


class PmaTableCoords(models.Model):
    db_name = models.CharField(max_length=64)
    table_name = models.CharField(max_length=64)
    pdf_page_number = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pma_table_coords'
        unique_together = (('db_name', 'table_name', 'pdf_page_number'),)


class PmaTableInfo(models.Model):
    db_name = models.CharField(max_length=64)
    table_name = models.CharField(max_length=64)
    display_field = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pma_table_info'
        unique_together = (('db_name', 'table_name'),)


class Pnotes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    message_status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'pnotes'


class Prescriptions(models.Model):
    patient_id = models.IntegerField(blank=True, null=True)
    filled_by_id = models.IntegerField(blank=True, null=True)
    pharmacy_id = models.IntegerField(blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    date_modified = models.DateField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    encounter = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    drug = models.CharField(max_length=150, blank=True, null=True)
    drug_id = models.IntegerField()
    rxnorm_drugcode = models.IntegerField(blank=True, null=True)
    form = models.IntegerField(blank=True, null=True)
    dosage = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.CharField(max_length=31, blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    route = models.IntegerField(blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    substitute = models.IntegerField(blank=True, null=True)
    refills = models.IntegerField(blank=True, null=True)
    per_refill = models.IntegerField(blank=True, null=True)
    filled_date = models.DateField(blank=True, null=True)
    medication = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    datetime = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    site = models.CharField(max_length=50, blank=True, null=True)
    prescriptionguid = models.CharField(max_length=50, blank=True, null=True)
    erx_source = models.IntegerField()
    erx_uploaded = models.IntegerField()
    drug_info_erx = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescriptions'


class Prices(models.Model):
    pr_id = models.CharField(max_length=11)
    pr_selector = models.CharField(max_length=255)
    pr_level = models.CharField(max_length=31)
    pr_price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'prices'
        unique_together = (('pr_id', 'pr_selector', 'pr_level'),)


class ProcedureAnswers(models.Model):
    procedure_order_id = models.BigIntegerField()
    procedure_order_seq = models.IntegerField()
    question_code = models.CharField(max_length=31)
    answer_seq = models.AutoField()
    answer = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'procedure_answers'
        unique_together = (('procedure_order_id', 'procedure_order_seq', 'question_code', 'answer_seq'),)


class ProcedureOrder(models.Model):
    procedure_order_id = models.BigIntegerField(primary_key=True)
    provider_id = models.BigIntegerField()
    patient_id = models.BigIntegerField()
    encounter_id = models.BigIntegerField()
    date_collected = models.DateTimeField(blank=True, null=True)
    date_ordered = models.DateField(blank=True, null=True)
    order_priority = models.CharField(max_length=31)
    order_status = models.CharField(max_length=31)
    patient_instructions = models.TextField()
    activity = models.IntegerField()
    control_id = models.CharField(max_length=255)
    lab_id = models.BigIntegerField()
    specimen_type = models.CharField(max_length=31)
    specimen_location = models.CharField(max_length=31)
    specimen_volume = models.CharField(max_length=30)
    date_transmitted = models.DateTimeField(blank=True, null=True)
    clinical_hx = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'procedure_order'


class ProcedureOrderCode(models.Model):
    procedure_order_id = models.BigIntegerField()
    procedure_order_seq = models.AutoField()
    procedure_code = models.CharField(max_length=31)
    procedure_name = models.CharField(max_length=255)
    procedure_source = models.CharField(max_length=1)
    diagnoses = models.TextField()
    do_not_send = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'procedure_order_code'
        unique_together = (('procedure_order_id', 'procedure_order_seq'),)


class ProcedureProviders(models.Model):
    ppid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    npi = models.CharField(max_length=15)
    send_app_id = models.CharField(max_length=255)
    send_fac_id = models.CharField(max_length=255)
    recv_app_id = models.CharField(max_length=255)
    recv_fac_id = models.CharField(max_length=255)
    dorp = models.CharField(db_column='DorP', max_length=1)  # Field name made lowercase.
    direction = models.CharField(max_length=1)
    protocol = models.CharField(max_length=15)
    remote_host = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    orders_path = models.CharField(max_length=255)
    results_path = models.CharField(max_length=255)
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'procedure_providers'


class ProcedureQuestions(models.Model):
    lab_id = models.BigIntegerField()
    procedure_code = models.CharField(max_length=31)
    question_code = models.CharField(max_length=31)
    seq = models.IntegerField()
    question_text = models.CharField(max_length=255)
    required = models.IntegerField()
    maxsize = models.IntegerField()
    fldtype = models.CharField(max_length=1)
    options = models.TextField()
    tips = models.CharField(max_length=255)
    activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'procedure_questions'
        unique_together = (('lab_id', 'procedure_code', 'question_code'),)


class ProcedureReport(models.Model):
    procedure_report_id = models.BigIntegerField(primary_key=True)
    procedure_order_id = models.BigIntegerField(blank=True, null=True)
    procedure_order_seq = models.IntegerField()
    date_collected = models.DateTimeField(blank=True, null=True)
    date_report = models.DateField(blank=True, null=True)
    source = models.BigIntegerField()
    specimen_num = models.CharField(max_length=63)
    report_status = models.CharField(max_length=31)
    review_status = models.CharField(max_length=31)
    report_notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'procedure_report'


class ProcedureResult(models.Model):
    procedure_result_id = models.BigIntegerField(primary_key=True)
    procedure_report_id = models.BigIntegerField()
    result_data_type = models.CharField(max_length=1)
    result_code = models.CharField(max_length=31)
    result_text = models.CharField(max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    facility = models.CharField(max_length=255)
    units = models.CharField(max_length=31)
    result = models.CharField(max_length=255)
    range = models.CharField(max_length=255)
    abnormal = models.CharField(max_length=31)
    comments = models.TextField()
    document_id = models.BigIntegerField()
    result_status = models.CharField(max_length=31)

    class Meta:
        managed = False
        db_table = 'procedure_result'


class ProcedureType(models.Model):
    procedure_type_id = models.BigIntegerField(primary_key=True)
    parent = models.BigIntegerField()
    name = models.CharField(max_length=63)
    lab_id = models.BigIntegerField()
    procedure_code = models.CharField(max_length=31)
    procedure_type = models.CharField(max_length=31)
    body_site = models.CharField(max_length=31)
    specimen = models.CharField(max_length=31)
    route_admin = models.CharField(max_length=31)
    laterality = models.CharField(max_length=31)
    description = models.CharField(max_length=255)
    standard_code = models.CharField(max_length=255)
    related_code = models.CharField(max_length=255)
    units = models.CharField(max_length=31)
    range = models.CharField(max_length=255)
    seq = models.IntegerField()
    activity = models.IntegerField()
    notes = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'procedure_type'


class ProductWarehouse(models.Model):
    pw_drug_id = models.IntegerField()
    pw_warehouse = models.CharField(max_length=31)
    pw_min_level = models.FloatField(blank=True, null=True)
    pw_max_level = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_warehouse'
        unique_together = (('pw_drug_id', 'pw_warehouse'),)


class Registry(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    directory = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)
    sql_run = models.IntegerField(blank=True, null=True)
    unpackaged = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registry'


class ReportItemized(models.Model):
    report_id = models.BigIntegerField()
    itemized_test_id = models.SmallIntegerField()
    numerator_label = models.CharField(max_length=25)
    pass_field = models.IntegerField(db_column='pass')  # Field renamed because it was a Python reserved word.
    pid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'report_itemized'


class ReportResults(models.Model):
    report_id = models.BigIntegerField()
    field_id = models.CharField(max_length=31)
    field_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_results'
        unique_together = (('report_id', 'field_id'),)


class RuleAction(models.Model):
    id = models.CharField(max_length=31)
    group_id = models.BigIntegerField()
    category = models.CharField(max_length=31)
    item = models.CharField(max_length=31)

    class Meta:
        managed = False
        db_table = 'rule_action'


class RuleActionItem(models.Model):
    category = models.CharField(max_length=31)
    item = models.CharField(max_length=31)
    clin_rem_link = models.CharField(max_length=255)
    reminder_message = models.TextField()
    custom_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rule_action_item'
        unique_together = (('category', 'item'),)


class RuleFilter(models.Model):
    id = models.CharField(max_length=31)
    include_flag = models.IntegerField()
    required_flag = models.IntegerField()
    method = models.CharField(max_length=31)
    method_detail = models.CharField(max_length=31)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rule_filter'


class RulePatientData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField()
    category = models.CharField(max_length=31)
    item = models.CharField(max_length=31)
    complete = models.CharField(max_length=31)
    result = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rule_patient_data'


class RuleReminder(models.Model):
    id = models.CharField(max_length=31)
    method = models.CharField(max_length=31)
    method_detail = models.CharField(max_length=31)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rule_reminder'


class RuleTarget(models.Model):
    id = models.CharField(max_length=31)
    group_id = models.BigIntegerField()
    include_flag = models.IntegerField()
    required_flag = models.IntegerField()
    method = models.CharField(max_length=31)
    value = models.CharField(max_length=255)
    interval = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'rule_target'


class Sequences(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sequences'


class SharedAttributes(models.Model):
    pid = models.BigIntegerField()
    encounter = models.BigIntegerField()
    field_id = models.CharField(max_length=31)
    last_update = models.DateTimeField()
    user_id = models.BigIntegerField()
    field_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'shared_attributes'
        unique_together = (('pid', 'encounter', 'field_id'),)


class StandardizedTablesTrack(models.Model):
    imported_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    revision_version = models.CharField(max_length=255)
    revision_date = models.DateTimeField(blank=True, null=True)
    file_checksum = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'standardized_tables_track'


class SupportedExternalDataloads(models.Model):
    load_id = models.BigIntegerField(unique=True)
    load_type = models.CharField(max_length=24)
    load_source = models.CharField(max_length=24)
    load_release_date = models.DateField()
    load_filename = models.CharField(max_length=256)
    load_checksum = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'supported_external_dataloads'


class SyndromicSurveillance(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lists_id = models.BigIntegerField()
    submission_date = models.DateTimeField()
    filename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'syndromic_surveillance'


class TemplateUsers(models.Model):
    tu_id = models.AutoField(primary_key=True)
    tu_user_id = models.IntegerField(blank=True, null=True)
    tu_facility_id = models.IntegerField(blank=True, null=True)
    tu_template_id = models.IntegerField(blank=True, null=True)
    tu_template_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_users'
        unique_together = (('tu_user_id', 'tu_template_id'),)


class Transactions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255)
    groupname = models.CharField(max_length=255)
    authorized = models.IntegerField(blank=True, null=True)
    refer_date = models.DateField(blank=True, null=True)
    refer_from = models.IntegerField()
    refer_to = models.IntegerField()
    refer_diag = models.CharField(max_length=255)
    refer_risk_level = models.CharField(max_length=255)
    refer_vitals = models.IntegerField()
    refer_external = models.IntegerField()
    refer_related_code = models.CharField(max_length=255)
    refer_reply_date = models.DateField(blank=True, null=True)
    reply_date = models.DateField(blank=True, null=True)
    reply_from = models.CharField(max_length=255)
    reply_init_diag = models.CharField(max_length=255)
    reply_final_diag = models.CharField(max_length=255)
    reply_documents = models.CharField(max_length=255)
    reply_findings = models.TextField()
    reply_services = models.TextField()
    reply_recommend = models.TextField()
    reply_rx_refer = models.TextField()
    reply_related_code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'transactions'


class UserSettings(models.Model):
    setting_user = models.BigIntegerField()
    setting_label = models.CharField(max_length=63)
    setting_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_settings'
        unique_together = (('setting_user', 'setting_label'),)


class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    fname = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    federaltaxid = models.CharField(max_length=255, blank=True, null=True)
    federaldrugid = models.CharField(max_length=255, blank=True, null=True)
    upin = models.CharField(max_length=255, blank=True, null=True)
    facility = models.CharField(max_length=255, blank=True, null=True)
    facility_id = models.IntegerField()
    see_auth = models.IntegerField()
    active = models.IntegerField()
    npi = models.CharField(max_length=15, blank=True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    specialty = models.CharField(max_length=255, blank=True, null=True)
    billname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_direct = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    assistant = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    valedictory = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=60, blank=True, null=True)
    streetb = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    street2 = models.CharField(max_length=60, blank=True, null=True)
    streetb2 = models.CharField(max_length=60, blank=True, null=True)
    city2 = models.CharField(max_length=30, blank=True, null=True)
    state2 = models.CharField(max_length=30, blank=True, null=True)
    zip2 = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    phonew1 = models.CharField(max_length=30, blank=True, null=True)
    phonew2 = models.CharField(max_length=30, blank=True, null=True)
    phonecell = models.CharField(max_length=30, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    cal_ui = models.IntegerField()
    taxonomy = models.CharField(max_length=30)
    ssi_relayhealth = models.CharField(max_length=64, blank=True, null=True)
    calendar = models.IntegerField()
    abook_type = models.CharField(max_length=31)
    pwd_expiration_date = models.DateField(blank=True, null=True)
    pwd_history1 = models.TextField(blank=True, null=True)
    pwd_history2 = models.TextField(blank=True, null=True)
    default_warehouse = models.CharField(max_length=31)
    irnpool = models.CharField(max_length=31)
    state_license_number = models.CharField(max_length=25, blank=True, null=True)
    newcrop_user_role = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersFacility(models.Model):
    tablename = models.CharField(max_length=64)
    table_id = models.IntegerField()
    facility_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_facility'
        unique_together = (('tablename', 'table_id', 'facility_id'),)


class UsersSecure(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    salt = models.CharField(max_length=255, blank=True, null=True)
    last_update = models.DateTimeField()
    password_history1 = models.CharField(max_length=255, blank=True, null=True)
    salt_history1 = models.CharField(max_length=255, blank=True, null=True)
    password_history2 = models.CharField(max_length=255, blank=True, null=True)
    salt_history2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_secure'
        unique_together = (('id', 'username'),)


class Version(models.Model):
    v_major = models.IntegerField()
    v_minor = models.IntegerField()
    v_patch = models.IntegerField()
    v_realpatch = models.IntegerField()
    v_tag = models.CharField(max_length=31)
    v_database = models.IntegerField()
    v_acl = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'version'


class X12Partners(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    id_number = models.CharField(max_length=255, blank=True, null=True)
    x12_sender_id = models.CharField(max_length=255, blank=True, null=True)
    x12_receiver_id = models.CharField(max_length=255, blank=True, null=True)
    x12_version = models.CharField(max_length=255, blank=True, null=True)
    processing_format = models.CharField(max_length=8, blank=True, null=True)
    x12_isa01 = models.CharField(max_length=2)
    x12_isa02 = models.CharField(max_length=10)
    x12_isa03 = models.CharField(max_length=2)
    x12_isa04 = models.CharField(max_length=10)
    x12_isa05 = models.CharField(max_length=2)
    x12_isa07 = models.CharField(max_length=2)
    x12_isa14 = models.CharField(max_length=1)
    x12_isa15 = models.CharField(max_length=1)
    x12_gs02 = models.CharField(max_length=15)
    x12_per06 = models.CharField(max_length=80)
    x12_gs03 = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'x12_partners'
