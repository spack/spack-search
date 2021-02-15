#!/bin/bash

# If the original migrations aren't run - do it.
# If you want to change models and run them again, you should run 
# these commands manually.
if [ ! -f "/opt/migrations-run" ]; then
    sleep 5
    python manage.py makemigrations source
    python manage.py migrate source
    python manage.py migrate
    python manage.py migrate admin
    python manage.py collectstatic --noinput
    touch /opt/migrations-run
fi

uwsgi nginx/uwsgi.ini
