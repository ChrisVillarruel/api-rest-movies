from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):

    """ Definimos la creación de un usuario comun """

    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('Asegurese de ingresar un nombre de usaurio')

        if email is None:
            raise TypeError('Asegurese de ingresar un correo valido')

        """ Definimos los cambios del modelo User """
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):

        if password is None:
            raise TypeError('Asegurese de haber ingresado un password')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


""" Sobreescribimos la clas AbstractBaseUser """


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    """ Remplazamos el metodo de logeo para utilizar el email como logeo """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
