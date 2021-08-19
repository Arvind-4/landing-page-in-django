from .base import *
import os
import django_heroku
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']

ADMIN_URL = os.environ.get('ADMIN_URL')

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

django_heroku.settings(locals())