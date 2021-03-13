# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# Lib
from django.db import models

# Local Modules
# from apps.api_classification.models import Classification
# from apps.api_movie_category.models import MovieCategory


# class Movies(models.Model):
#     pass
# movie_id = models.AutoField(primary_key=True)
# name_movie = models.CharField(unique=True, max_length=100)
# launch_year = models.IntegerField()
# sinopsis = models.CharField(max_length=255)
# duration = models.CharField(max_length=20)
# category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE, related_name='category')
# classification = models.ForeignKey(Classification, on_delete=models.CASCADE, related_name='classification')

# class Meta:
#     # managed = False
#     db_table = 'tbl_movies'
#     verbose_name = 'Pelicula'
#     verbose_name_plural = 'Peliculas'
#     ordering = ['movie_id']

# def __str__(self):
#     return f'{self.name_movie.title()}, {self.launch_year}, {self.duration}'
