#!/bin/sh
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn Blog_Project.wsgi:application \
  --bind 0.0.0.0:8000
