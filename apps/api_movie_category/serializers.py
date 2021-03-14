from rest_framework import serializers

from .models import MovieCategory


class MovieCategorySerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(max_length=100, min_length=5)
    category_desc = serializers.CharField(max_length=250)

    class Meta:
        model = MovieCategory
        exclude = ('state', 'created_at', 'updated_at', 'deleted_at')

    def validate_category_name(self, value):
        category_name = value

        if category_name.isnumeric():
            msg = 'Asegurese que este campo contenga unicamente caracteres alfabeticos'
            raise serializers.ValidationError(msg)

        if MovieCategory.objects.filter(category_name=category_name).exists():
            msg = 'Ya existe una categoria con este nombre'
            raise serializers.ValidationError(msg)

        return value

    def validate_category_desc(self, value):
        category_desc = value

        if category_desc.isnumeric():
            raise serializers.ValidationError(
                'Asegurese que este campo contenga unicamente caracteres alfabeticos')
        return value

    def create(self, validate_data):
        return MovieCategory.objects.create(**validate_data)
