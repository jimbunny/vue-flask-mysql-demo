#!/usr/bin/env bash
#python manager.py db init &&
python manager.py db migrate &&
python manager.py db upgrade &&
#gunicorn django_web_app.wsgi:application -w 2 -b :8000
python manager.py run