from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_views
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'records/patient-data', views.PatientDataViewSet)
router.register(r'records/history-data', views.HistoryDataViewSet)
router.register(r'records/medical-history', views.MedicalHistoryViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),  # API Routing
    url(r'^token/$', rest_views.obtain_auth_token),  # POST to get token
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),  # Authenticate to API
    url(r'^records/(?P<pid>[0-9]+)/history-data', views.ListHistoryData.as_view())  # Return a list of visits based on pid
]
