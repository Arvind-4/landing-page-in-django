from decouple import config

DJANGO_LIVE = config('DJANGO_LIVE', cast=bool)

if DJANGO_LIVE:
    print("Production settings loaded")
    from .production import *

else:
    print("Development settings loaded")
    from .local import *