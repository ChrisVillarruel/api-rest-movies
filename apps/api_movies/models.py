# Modulos nativos django
from django.db import models

# Modulos locales
from apps.api_classification.models import Classification
from apps.api_movie_category.models import MovieCategory
from apps.base.models import BaseModel


class Movies(BaseModel):
    # Modelo que hereda de Base model para la creación de una pelicula

    movie_id = models.AutoField(primary_key=True)
    name_movie = models.CharField(unique=True, max_length=100)
    launch_year = models.IntegerField()
    sinopsis = models.CharField(max_length=255)
    duration = models.CharField(max_length=20)
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE, related_name='category')
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, related_name='classification')

    class Meta:
        db_table = 'tbl_movies'
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'
        ordering = ['movie_id']

    def __str__(self):
        return f'{self.name_movie.title()}, {self.launch_year}, {self.duration}'
