# Generated by Django 3.1 on 2021-03-13 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_classification', '0002_auto_20210312_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='classification_name',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]