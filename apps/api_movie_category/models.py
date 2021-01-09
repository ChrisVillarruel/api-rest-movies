from django.db import models


class MovieCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(unique=True, max_length=100)
    category_desc = models.CharField(max_length=100, blank=True, null=True, default='Sin descripción')

    class Meta:
        managed = False
        db_table = 'tbl_movie_category'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['category_id']

    def __str__(self):
        return f'{self.category_id}: {self.category_name.title()}, {self.category_desc}'
