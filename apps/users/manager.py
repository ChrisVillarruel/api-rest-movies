from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None): 

        if username is None:
            raise TypeError('Error. Ingrese un nombre de usuario valido.')

        if email is None:
            raise TypeError('Error. Ingrese una dirección de correo electronico valido.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        
        if password is None:
            raise TypeError('Error. Ingrese una contraseña.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


    
