from django.contrib import admin
from api.models import PatientData, HistoryData, InsuranceData, FormEncounter, IssueEncounter, Forms, Lists, ListsTouch, Facility, FormVitals, FormRos, FormReviewofs
# Register your models here.

admin.site.register(PatientData)
admin.site.register(HistoryData)
admin.site.register(InsuranceData)
admin.site.register(FormEncounter)
admin.site.register(IssueEncounter)
admin.site.register(Forms)
admin.site.register(Lists)
admin.site.register(ListsTouch)
admin.site.register(Facility)
admin.site.register(FormVitals)
admin.site.register(FormRos)
admin.site.register(FormReviewofs)
