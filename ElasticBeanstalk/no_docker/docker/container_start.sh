#!/bin/sh
cd /var/projects/openemr_api_project && python manage.py migrate --noinput
supervisord -n -c /etc/supervisor/supervisord.conf