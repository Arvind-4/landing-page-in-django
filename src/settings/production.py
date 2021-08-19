from .base import *
import os
import django_heroku

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']

ADMIN_URL = os.environ.get('ADMIN_URL')

django_heroku.settings(locals())