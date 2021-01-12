from rest_framework import serializers
from datetime import datetime

from .models import Movies
from apps.api_classification.models import Classification
from apps.api_movie_category.models import MovieCategory


class MoviesSerializer(serializers.ModelSerializer):
    name_movie = serializers.CharField(max_length=100, min_length=5)
    launch_year = serializers.IntegerField()
    sinopsis = serializers.CharField(max_length=255)
    duration = serializers.CharField(max_length=20)

    class Meta:
        model = Movies
        fields = ['movie_id', 'name_movie', 'launch_year', 'sinopsis', 'duration', 'category', 'classification']

    # custom list
    def to_representation(self, instance):
        return {
            'id': instance['movie_id'],
            'name': instance['name_movie'],
            'launch_year': instance['launch_year'],
        }

    # validate serializers fields
    def validate_name_movie(self, value):
        name_movie = value

        if name_movie.isnumeric():
            raise serializers.ValidationError(
                'Asegurese que este campo contenga unicamente caracteres alfabeticos')

        return value.title()

    def validate_launch_year(self, value):
        launch_year = value
        actual_year = int(datetime.now().strftime("%Y"))

        if launch_year > actual_year or launch_year < 1922:
            raise serializers.ValidationError(
                f'El año que usted ingreso no es valido. Asegurese que el año se encuentre entre {actual_year} y el año 1922')
        return value

    def validate_duration(self, value):
        duration = value

        if len(duration) > 3:
            raise serializers.ValidationError(
                'Asegurese que haya ingresado el numero de minutos valido, no deberia de ser mayor a 3 digitos')

        return f'{value} Minutos'

    def create(self, validate_data):
        return Movies.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name_movie = validate_data.get('name_movie', instance.name_movie)
        instance.launch_year = validate_data.get('launch_year', instance.launch_year)
        instance.sinopsis = validate_data.get('sinopsis', instance.sinopsis)
        instance.duration = validate_data.get('duration', instance.duration)
        instance.category = validate_data.get('category', instance.category)
        instance.classification = validate_data.get('classification', instance.classification)
        instance.save()
        return instance


class MoviesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'
        depth = 1
