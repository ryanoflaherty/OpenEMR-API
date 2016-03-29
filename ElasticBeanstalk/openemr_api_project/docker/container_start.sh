#!/bin/sh
cd /var/projects/openemr_api_project && python manage.py migrate --noinput
#python manage.py collectstatic --noinput
supervisord -n -c /etc/supervisor/supervisord.conf
