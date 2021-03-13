# Modulos nativos de django
from django.db import models

# Modulos locales
from apps.base.models import BaseModel


class MovieCategory(BaseModel):
    # Modelo que hereda de Base model. Cada pelicula debe de tener una categoria

    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(unique=True, max_length=100)
    category_desc = models.CharField(max_length=250, null=False)

    class Meta:
        db_table = 'tbl_movie_category'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['category_id']

    def __str__(self):
        return f'{self.category_name}'
