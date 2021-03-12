from django.db import models

# Modulo local
from apps.base.models import BaseModel


class Classification(BaseModel):
    # Modelo que hereda de Base model. Cada pelicula debe de tener clasificación

    classification_id = models.AutoField(primary_key=True)
    classification_name = models.CharField(max_length=3)
    classification_desc = models.CharField(unique=True, max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_classification'
        verbose_name = 'Clasificación'
        verbose_name_plural = 'Clasificaciones'
        ordering = ['classification_id']

    def __str__(self):
        return f'{self.classification_name.upper()}'
