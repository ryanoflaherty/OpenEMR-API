from django.conf.urls import url, include
from rest_framework.authtoken import views as rest_views
from api import views


"""
API Endpoints for authentication, API root
"""
urlpatterns = [
    url(r'^$', views.api_root), # API Root for browsable API
    url(r'^token/$', views.ObtainExpiringAuthToken.as_view())
    #url(r'^token/$', rest_views.obtain_auth_token),  # POST to get token
    #url(r'^auth', include('rest_framework.urls', namespace='rest_framework'), name='auth'),  # Session Authenticate to API
]

"""
API Endpoints for app functionality
"""
urlpatterns += [
    url(r'^test/$', views.MetadataView.as_view(), name='old-medical-record-create-update'), # OLD Create a new Medical History object
    url(r'^records/$', views.create_visit, name='medical-record-create-update'),   # Create a new Medical History object
    url(r'^records/patient-data', views.PatientDataList.as_view(), name='patient-data-list'),   # Return a filtered list of Patient Data objects
    url(r'^records/(?P<pubpid>[0-9]+)/visits', views.list_visits, name='visits-list'),  # Return a list of visits based on pid
    #url(r'^users', views.UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='users'),
]