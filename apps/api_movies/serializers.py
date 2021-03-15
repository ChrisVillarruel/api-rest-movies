# Modulos nativos de rest_framework
from rest_framework import serializers
from datetime import datetime

# Modulos locales
from .models import Movies
from apps.api_classification.models import Classification
from apps.api_movie_category.models import MovieCategory


class MoviesSerializer(serializers.ModelSerializer):
    # Serializador para la creación de una pelicula

    name_movie = serializers.CharField(max_length=100, min_length=5)
    launch_year = serializers.IntegerField()
    sinopsis = serializers.CharField(max_length=255)
    duration = serializers.CharField(max_length=20)

    class Meta:
        model = Movies
        exclude = ('state', 'created_at', 'updated_at', 'deleted_at')

    def to_representation(self, instance):
        # Listado de una pelicula personalizado

        return {
            'movie_id': instance.movie_id,
            'name_movie': instance.name_movie,
            'launch_year': instance.launch_year,
            'duration': instance.duration,
            'sinopsis': instance.sinopsis,
            'category': instance.category.category_name,
            'classification': instance.classification.classification_name
        }

    def validate_name_movie(self, value):
        # Validamos el nombre de la pelicula

        if value.isnumeric():
            msg = 'Asegurese que este campo contenga unicamente caracteres alfabeticos'
            raise serializers.ValidationError(msg)

        if Movies.objects.filter(name_movie=value).exists():
            msg = f'Ya existe una pelicula con el nombre {value.upper()}'
            raise serializers.ValidationError(msg)

        return value.title()

    def validate_launch_year(self, value):
        actual_year = int(datetime.now().strftime("%Y"))

        if value > actual_year or value < 1922:
            msg = f'El año que usted ingreso no es valido. Asegurese que el año se encuentre entre {actual_year} y el año 1922'
            raise serializers.ValidationError(msg)

        return value

    def validate_duration(self, value):
        if len(value) > 3:
            msg = 'Asegurese que haya ingresado el numero de minutos valido, no deberia de ser mayor a 3 digitos'
            raise serializers.ValidationError(msg)

        return f'{value} Minutos'
