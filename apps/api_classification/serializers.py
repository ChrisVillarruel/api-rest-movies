from rest_framework import serializers
from .models import Classification


class ClassificationSerializer(serializers.ModelSerializer):
    classification_name = serializers.CharField(max_length=3, min_length=1)
    classification_desc = serializers.CharField(max_length=100)

    class Meta:
        model = Classification
        fiedls = ['classification_name', 'classification_desc']

    # listado personalizado
    def to_representation(self, instance):
        return {
            'classification_id': instance['classification_id'],
            'classification_name': instance['classification_name'],
            'classification_desc': instance['classification_desc']
        }

    # validaciones classification_desc
    def validate_classification_name(self, value):
        classification_name = value

        if classification_name.isnumeric():
            raise serializers.ValidationError(
                'Asegurese que este campo contenga unicamente caracteres alfanumericos')

        if not classification_name.isalpha():
            raise serializers.ValidationError(
                'Asegurese que este campo no contenga caracteres especiales')

        return value

    # validaciones classification_desc
    def validate_classification_desc(self, value):
        classification_desc = value

        if classification_desc.isnumeric():
            raise serializers.ValidationError(
                'Asegurese que este campo contenga unicamente caracteres')

        if classification_desc is None:
            classification_desc = 'Sin descripción'
            return classification_desc

        return value.capitalize()

    # campos validados

    def validate(self, data):
        return data

    # create
    def create(self, validate_data):
        return Classification.objects.create(**validate_data)

    # update
    def update(self, instance, validate_data):
        instance.classification_name = validate_data.get('classification_id', instance.classification_name)
        instance.classification_desc = validate_data.get('classification_desc', instance.classification_desc)
        instance.save()
        return instance


class ClassificationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ['classification_id', 'classification_name', 'classification_desc']
