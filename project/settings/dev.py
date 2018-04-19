from .base import *

DEBUG = True
ENVIRON = ENVIRONS['dev']


INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
    'rest_framework_swagger',
    'rest_framework',
    'drf_yasg',
    'django.contrib.admindocs',
]


MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'utils.middleware.CORSMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',  # for heroku
]

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['127.0.0.1', 'localhost']

INTERNAL_IPS = ['127.0.0.1']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

###################
# CUSTOM SETTINGS #
###################

CSRF_CHECK = False

ACCESS_CONTROL_ALLOW_ORIGIN = '*'

USE_CELERY = True
