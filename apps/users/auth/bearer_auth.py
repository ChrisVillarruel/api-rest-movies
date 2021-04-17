
# modulo de jwt
import jwt

# Modulo nativo de rest_framework 
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions 

# Modulo nativo de django
from django.conf import settings

# Modulo local
from apps.users.models import User


class JWTAuthentication(BaseAuthentication):
    # Tipo de prefijo que sera utilizado al autenticarse
    prefix_header_authentication = 'Bearer'

    def authenticate(self, request):

        # Se determina la petición vacia porque por defecto no se esta autenticado
        request.user = None

        # Devuelve una cadena bytes del header autorization y lo convertimos en un lista con split
        auth_header = get_authorization_header(request).split()

        # seleccionamos el prefijo que vamos a utilizar 
        auth_prefix_header = self.prefix_header_authentication.lower()
 
        if not auth_header:
            # Si no hay una autenticación 

            msg = 'Debes iniciar sesión para realizar esta acción.'
            raise exceptions.AuthenticationFailed(msg)
            return None

        if len(auth_header) == 1:
            # Si la logintud es igual a uno quiere decir que no se ha proveeido ningun token token 

            msg = 'No se proveyó el token de autorización.'
            raise exceptions.AuthenticationFailed(msg)
            
        if len(auth_header) > 2:
            # Si hay mas elementos dentro auth_token, queire decir que existen espación en blanco dentro del token
            # por lo tanto el token es invalido

            msg = 'Token invalido y/o tiene errores ortograficos.'
            raise exceptions.AuthenticationFailed(msg)

        # Decoficamos el prefijo y el token utlizando el estandar utf-8
        prefix = auth_header[0].decode('utf-8')
        jwt_token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_prefix_header:
            # Si el prefijo es diferente al prefijo que se esperaba retorna un error

            msg = 'Error Token no identificado.'
            raise exceptions.AuthenticationFailed(msg)


        """
        Si el token llego hasta aqui, quiere decir que token paso las primeras        
        validaciones y se confirma que el token es de la propiedad del sistema. 
        Ahora bien no significa que ya se tiene acceso pues ahora se deberan de
        autenticar las crendeciales de acceso.


        """
        return self._authenticate_credentials(request, jwt_token)


    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            type_token = payload['token']
            

            if type_token == 'access':
               user = User.objects.get(access_token=token)
            
            if type_token == 'refresh':
                user = User.objects.get(refresh_token=token)
                

            if not user.is_active:
                msg = 'El usuario al que intenta autenticarse fue desactivado.'
                raise exceptions.AuthenticationFailed(msg)

        except jwt.ExpiredSignatureError as e:
            msg = 'Token de autenticación expirado.'
            raise exceptions.AuthenticationFailed(msg)

        except jwt.exceptions.DecodeError as e:
            msg = 'Ocurrio un error al decodificar el token.'
            raise exceptions.AuthenticationFailed(msg)

        except User.DoesNotExist as e:
            msg = 'El token de autenticación no existe o fue eliminado.'
            raise exceptions.AuthenticationFailed(msg)


        return (user, token)






