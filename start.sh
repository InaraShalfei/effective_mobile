#!/bin/bash

cd orders
python manage.py makemigrations users
python manage.py migrate users
python manage.py makemigrations cafe_orders
python manage.py migrate cafe_orders
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn orders.wsgi:application --log-level=debug --bind 0.0.0.0:8000 --reload