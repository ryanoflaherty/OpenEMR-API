from django.conf.urls import url, include
from rest_framework.authtoken import views as rest_views
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#router.register(r'records/patient-data', views.PatientDataViewSet)
#router.register(r'records/history-data', views.HistoryDataViewSet)
#router.register(r'records/medical-history', views.MedicalHistoryViewSet)


"""
API Endpoints for authentication, API root
"""
urlpatterns = [
    url(r'^$', views.api_root), # API Root for browsable API
    url(r'^viewsets', include(router.urls)),  # API Router for testing
    url(r'^token/$', rest_views.obtain_auth_token),  # POST to get token
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework'), name='auth'),  # Authenticate to API
]

"""
API Endpoints for app functionality
"""
urlpatterns += [
    url(r'^records/$', views.CreateUpdateMedicalRecord.as_view(), name='medical-record-create-update'), # Create a new Medical History object
    url(r'^records/(?P<pid>[0-9]+)/history-data', views.HistoryDataList.as_view(), name='history-data-list'),  # Return a list of visits based on pid
    url(r'^records/patient-data', views.PatientDataList.as_view(), name='patient-data-list'),   # Return a filtered list of Patient Data objects
    url(r'^users', views.UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='users'),
    url(r'^groups', views.GroupViewSet.as_view({'get': 'list'}), name='groups'),
]