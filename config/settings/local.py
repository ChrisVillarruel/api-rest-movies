from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {},
    'windows': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moviesdb',
        'USER': 'chris',
        'PASSWORD': 'givc980909',
        'HOST': 'localhost',
        'PORT': 3306,
    },
    'linux': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moviesdb',
        'USER': 'chris',
        'PASSWORD': 'givc980909',
        'HOST': 'localhost',
        'PORT': 3307,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
