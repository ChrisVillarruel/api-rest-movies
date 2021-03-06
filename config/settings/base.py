
from pathlib import Path
import os
from . import database_info


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i9@wh167(d2+vyc2f696lafrk8f4gvavb)#2(00of=64_^s_x&'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# app local
LOCAL_APPS = [
    'apps.base',
    'apps.api_classification',
    'apps.api_movie_category',
    'apps.api_movies',
    'apps.users',
]

# third apps
THIRD_APPS = [
    'rest_framework',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'exception_handler.custom_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_PAGINATION_CLASS': 'pagination.StandardResultsSetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': ('apps.users.auth.bearer_auth.JWTAuthentication',)
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

"""
Si usted clono el repositorio ingrese sus propias credenciales
de su base de datos.

Si usted desea utilizar otro cliente de base de datos, modifique
ENGINE.


"""

ENGINE = 'django.db.backends.mysql'
NAME_SCHEMA = database_info.NAME_SCHEMA
USERNAME = database_info.USERNAME
PASSWORD = database_info.PASSWORD
HOST = database_info.HOST
PORT = database_info.PORT


# Modelo usuario personalizado
AUTH_USER_MODEL = 'users.User'


