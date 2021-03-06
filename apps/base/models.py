from django.db import models


class BaseModel(models.Model):
    # Modelo base para los demas modelos


    state = models.BooleanField(default=True)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class UserToken(models.Model):
    access_token = models.CharField(max_length=500, null=True, default=None, blank=True)
    refresh_token = models.CharField(max_length=500, null=True, default=None, blank=True)

    class Meta:
        abstract = True

