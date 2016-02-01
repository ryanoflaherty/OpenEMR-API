from django.contrib import admin
from api.models import Users, PatientData, HistoryData, InsuranceData
# Register your models here.

admin.site.register(Users)
admin.site.register(PatientData)
admin.site.register(HistoryData)
admin.site.register(InsuranceData)
