from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_views
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'patient-data', views.PatientDataViewSet)
router.register(r'history-data', views.HistoryDataViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),  # API Routing
    url(r'^token/$', rest_views.obtain_auth_token),  # POST to get token
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),  # Authenticate to API
]
