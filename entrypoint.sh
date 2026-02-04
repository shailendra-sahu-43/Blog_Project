#!/bin/sh
set -e

cd /app

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn Blog_Project.wsgi:application \
  --chdir /app \
  --bind 0.0.0.0:8000
