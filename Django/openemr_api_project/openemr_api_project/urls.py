"""openemr_api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from api import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),  # Home Page for logged in users
    url(r'^remotehcs/', views.index_guest, name='index-guest'), # landing page for visiters
    url(r'^api/', include('api.urls')),   # Route to all API calls
    url(r'^admin/', admin.site.urls),   # Admin portal
    url(r'^users/manage/', views.user_management, name='user-management'),
    url(r'^users/overview/', views.user_overview, name='user-overview'),
    url(r'^analytics/', views.analytics, name='analytics'),
    url(r'^help/$', views.help, name='help'),
    url(r'^about/$', views.about, name='about'),
]

# Auth URLs
# TODO Implement these forms - https://github.com/django/django/blob/master/django/contrib/auth/forms.py
urlpatterns += [
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/password_change/$', views.password_change, name='change-password'),
    url(r'^accounts/password_change/done/$', views.password_change_done, name='change-password-done'),
    url(r'^accounts/password_reset/$', views.logout, name='reset-password'),
    url(r'^accounts/password_reset/done/$', views.logout, name='reset-password-done'),
    url(r'^accounts/register/$, views.logout', views.logout, name='register'),
    url(r'^accounts/register/done/$', views.logout, name='register'),
]