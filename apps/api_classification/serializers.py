from rest_framework import serializers
from .models import Classification


class ClassificationSerializer(serializers.ModelSerializer):
    classification_name = serializers.CharField(max_length=3, min_length=1)
    classification_desc = serializers.CharField(max_length=250)

    class Meta:
        model = Classification
        exclude = ('state', 'created_at', 'updated_at', 'deleted_at')

    def to_representation(self, instance):
        # retorna un listado personalizado

        return {
            'classification_id': instance['classification_id'],
            'classification_name': instance['classification_name'],
            'classification_desc': instance['classification_desc']
        }

    def validate_classification_name(self, value):
        # retornara el nombre de la clasificación simepre y cuando las condiciones sean falsas

        if value.isnumeric():
            msg = 'Asegurese que este campo contenga unicamente caracteres alfanumericos'
            raise serializers.ValidationError(msg)

        if not value.isalpha():
            msg = 'Asegurese que este campo no contenga caracteres especiales'
            raise serializers.ValidationError(msg)

        if Classification.objects.filter(classification_name=value):
            msg = f'Ya existe una clasificacion con este nombre {value.upper()}.'
            raise serializers.ValidationError(msg)

        return value.upper()

    def validate_classification_desc(self, value):
        # retornara la descripción de la clasificación, si todas la condiciones sean flasas

        if value.isnumeric():
            msg = 'Asegurese que este campo contenga unicamente caracteres'
            raise serializers.ValidationError(msg)

        return value.capitalize()

    def create(self, validate_data):
        return Classification.objects.create(**validate_data)
