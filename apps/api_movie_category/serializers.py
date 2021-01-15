from rest_framework import serializers

from .models import MovieCategory


class CategorySerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(max_length=100, min_length=5)
    category_desc = serializers.CharField(max_length=250, min_length=5, allow_blank=True)

    class Meta:
        model = MovieCategory
        fields = ['category_id', 'category_name', 'category_desc']

    def validate_category_name(self, value):
        category_name = value

        if category_name.isnumeric():
            raise serializers.ValidationError(
                'Asegurese que este campo contenga unicamente caracteres alfabeticos')

        if MovieCategory.objects.filter(category_name=category_name).exists():
            raise serializers.ValidationError(
                f'Ya existe una categoria con el nombre {category_name.upper()}')

        return value

    def validate_category_desc(self, value):
        category_desc = value

        if category_desc.isnumeric():
            raise serializers.ValidationError(
                'Asegurese que este campo contenga unicamente caracteres alfabeticos')
        return value

    def validate(self, data):
        return data

    def create(self, validate_data):
        return MovieCategory.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.category_name = validate_data.get('category_name', instance.category_name)
        instance.category_desc = validate_data.get('category_desc', instance.category_desc)
        instance.save()
        return instance
