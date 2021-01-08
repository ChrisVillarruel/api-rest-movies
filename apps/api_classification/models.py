from django.db import models


class Classification(models.Model):
    classification_id = models.AutoField(primary_key=True)
    classification_name = models.CharField(max_length=3)
    classification_desc = models.CharField(unique=True, max_length=100, blank=True, null=True, default='Sin descripción')

    class Meta:
        managed = False
        db_table = 'tbl_classification'
        verbose_name = 'Clasificación'
        verbose_name_plural = 'Clasificaciones'
        ordering = ['classification_id']

    def __str__(self):
        return f'{self.classification_id}: {self.classification_name.upper()}, {self.classification_desc}'
