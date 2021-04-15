# Modulos JWT
import jwt

# Modulos de python
from django.conf import settings

# modulos locales
from .timezone import generate_expire_token, get_timezone

def generate_token(email, username, days=0, minutes=0):
    jwt_token = jwt.encode({
        'email': email,
        'username': username,
        'type': 'bearer',
        'exp': generate_expire_token(days=days, minutes=minutes), 
        'iat': get_timezone()
    }, settings.SECRET_KEY, algorithm='HS256')

    return jwt_token.decode('utf-8')


