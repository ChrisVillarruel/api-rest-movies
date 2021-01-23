from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # Este campo se puede utilizar para creación o actualización de una instancia
    # pero no se incluye en el momento de serializar la presenteción
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_password(self, value):
        password = value
        li = []

        # Verificar caracteres prohibidos
        for p in password:
            if not p.isalnum():
                li.append(p)

        if not password.isalnum():
            raise serializers.ValidationError(
                f'Contraseña Erronea. Asegurese que la contraseña no contenga caracteres especiales {(li)}')
        return value

    def validate_email(self, value):
        email = value

        # Consultamos si ya existe el email actual
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                f'El correo que ingreso ya existe. Ingrese uno distinto a {email}')
        return value.lower()

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4)
    password = serializers.CharField(max_length=64, min_length=8, write_only=True)
