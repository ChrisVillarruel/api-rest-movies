
# Modulo de JWT
import jwt

# Modulo nativo de django
from datetime import datetime
from django.conf import settings

# Modulo nativo de rest_framework
from rest_framework import exceptions

# Modulo local
from .timezone import get_timezone

def get_expired_date_token(token):
    """
    retornamos la fecha de expiración en formato "Y-M-D"
    del token entrante


    """

    try:
        payload = jwt.decode(token, settings.SECRET_KEY)
        
        # De la fecha de expiración restale cinco dias antes de la expiración
        get_date_expired = payload['exp'] - 432000

        return datetime.fromtimestamp(get_date_expired).strftime('%y%m%d')
    except jwt.exceptions.DecodeError as e:
        msg = 'Error al decodificar el token'
        raise exceptions.AuthenticationFailed(msg)

    except jwt.exceptions.ExpiredSignatureError as e:
        # Si el token ya caduco, retorna la fecha actual

        return get_timezone().strftime('%y%m%d')
        
