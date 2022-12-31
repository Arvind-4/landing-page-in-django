from decouple import config

DJANGO_LIVE = config('DJANGO_LIVE', cast=bool)

if DJANGO_LIVE:
    from .production import *

else:
    from .local import *