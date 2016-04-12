from django.conf.urls import url, include
from rest_framework.authtoken import views as rest_views
from api import views


"""
API Endpoints for authentication, API root
"""
urlpatterns = [
    url(r'^$', views.api_root), # API Root for browsable API
    url(r'^token/$', rest_views.obtain_auth_token),  # POST to get token
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework'), name='auth'),  # Session Authenticate to API
]

"""
API Endpoints for app functionality
"""
urlpatterns += [
    url(r'^records/$', views.CreateUpdateMedicalRecord.as_view(), name='medical-record-create-update'), # Create a new Medical History object
    url(r'^test/$', views.create_visit, name='new-medical-record-create-update'),   # Create a new Medical History object
    url(r'^records/patient-data', views.PatientDataList.as_view(), name='patient-data-list'),   # Return a filtered list of Patient Data objects
    url(r'^records/(?P<pubpid>[0-9]+)/visits', views.list_visits, name='visits-list'),  # Return a list of visits based on pid
    url(r'^test/(?P<pubpid>[0-9]+)/visits', views.VisitsHistoryList.as_view(), name='old-visits-list'), # Return a list of forms + hd based on pid
    #url(r'^users', views.UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='users'),
]