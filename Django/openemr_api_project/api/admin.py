from django.contrib import admin
from api.models import PatientData, HistoryData, InsuranceData
# Register your models here.

admin.site.register(PatientData)
admin.site.register(HistoryData)
admin.site.register(InsuranceData)
