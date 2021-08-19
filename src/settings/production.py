from .base import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']

ADMIN_URL = os.environ.get('ADMIN_URL')

