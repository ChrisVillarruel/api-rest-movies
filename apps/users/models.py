# Modulos nativos de django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Modulos locales
from . import manager
from apps.base.models import BaseModel, UserToken
from .auth.generate_token import generate_token 
from .auth.timezone import get_timezone
from .auth.generate_token import generate_token
from .auth.get_expired_token import get_expired_date_token

class User(AbstractBaseUser, PermissionsMixin, BaseModel, UserToken):
    user_id = models.AutoField(auto_created=True, primary_key=True, serialize=True)
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=110, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=255, null=True, blank=True, default='Sin nombre')
    last_name = models.CharField(max_length=255, null=True, blank=True, default='Sin apellidos')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = manager.UserManager()
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'tbl_users'
        ordering = ['-user_id']

    def __str__(self):
        return f'{self.email}: {self.username}'

    def get_email(self):
        return self.email.lower()

    def get_fullname(self):
        full_name = f'{first_name.title()} {last_name.title()}'
        return full_name

    def token():
        """
        Retornamos los tokens de autorización 


        """
        return {
            'access_token':self.access_token, 
            'refresh_token':self.refresh_token
        }


    def save(self, *args, **kwargs):
        current_date = get_timezone().strftime('%y%m%d')
        
        if self.access_token is None and self.refresh_token is None:
            self.access_token = generate_token(self.get_email(), self.username, token='access', minutes=30)
            self.refresh_token = generate_token(self.get_email(), self.username, token='refresh', days = 60)

        if current_date >= get_expired_date_token(self.refresh_token):                        
            self.refresh_token = generate_token(self.get_email(), self.username, token='refresh', days=60)


        super().save(*args, **kwargs)





