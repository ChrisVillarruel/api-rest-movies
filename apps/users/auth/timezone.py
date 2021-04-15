
# Modulos nativos de django
from django.conf import settings

# Modulos de python
import datetime
import pytz 
from datetime import timedelta


def get_timezone():
    return datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE))


def generate_expire_token(days=0, minutes=0):
    return get_timezone() + datetime.timedelta(days=days, minutes=minutes)
