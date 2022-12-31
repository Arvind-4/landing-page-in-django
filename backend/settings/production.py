from decouple import config

from .base import *

SECRET_KEY = config('DJANGO_SECRET_KEY', cast=str)

DEBUG = config('DJANGO_DEBUG', cast=bool)

ALLOWED_HOSTS = ['*']

ADMIN_URL = config('DJANGO_ADMIN_URL', cast=str)

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

STATIC_ROOT = BASE_DIR / 'staticfiles_build' / 'static'

from backend.db.postgres_db import * # noqa