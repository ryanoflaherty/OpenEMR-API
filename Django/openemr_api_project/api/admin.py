from django.contrib import admin
from api.models import PatientData, HistoryData, FormEncounter, IssueEncounter, Forms, Lists, Facility, FormVitals, FormRos, FormReviewofs, MedicalHistory, Visit
# Register your models here.

admin.site.register(PatientData)
admin.site.register(HistoryData)
admin.site.register(FormEncounter)
admin.site.register(IssueEncounter)
admin.site.register(Forms)
admin.site.register(Lists)
admin.site.register(Facility)
admin.site.register(FormVitals)
admin.site.register(FormRos)
admin.site.register(FormReviewofs)
admin.site.register(MedicalHistory)
admin.site.register(Visit)
