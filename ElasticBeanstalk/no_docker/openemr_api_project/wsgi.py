"""
WSGI config for openemr_api_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

import django.core.handlers.wsgi 
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ec2-user/OpenEMR-API/Django/openemr_api_project')
sys.path.append('/home/ec2-user/OpenEMR-API/Django/openemr_api_project/openemr_api_project')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openemr_api_project.settings")

application = get_wsgi_application()
#application = django.core.handlers.wsgi.WSGIHandler()
