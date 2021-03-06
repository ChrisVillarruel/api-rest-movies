from django.db import models

# Modulo local
from apps.base.models import BaseModel


class Classification(BaseModel):
    # Modelo que hereda de Base model. Cada pelicula debe de tener una clasificación

    classification_id = models.AutoField(primary_key=True)
    classification_name = models.CharField(max_length=3, unique=True)
    classification_desc = models.CharField(unique=True, max_length=250, null=False)

    class Meta:
        db_table = 'tbl_classification'
        verbose_name = 'Clasificación'
        verbose_name_plural = 'Clasificaciones'
        ordering = ['classification_id']

    def __str__(self):
        return f'{self.classification_name.upper()}'
