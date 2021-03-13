# Modulos nativos rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Modulo de python
from datetime import datetime

# Modulos Locales
from .serializers import ClassificationSerializer
from apps.metodosExternos import msg_error, msg_success
from .models import Classification


class ClassificationViewSet(ModelViewSet):
    serializer_class = ClassificationSerializer

    def get_queryset(self, pk=None):
        # Si pk es None, retornamos un listado. De lo contrario retornamos un objeto

        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True).values(
                'classification_id', 'classification_name', 'classification_desc')

        return self.get_serializer().Meta.model.objects.filter(classification_id=pk, state=True).first()

    def create(self, request):
        # Creación de una Clasificación

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        success = msg_success('Clasificación creada', 201)
        return Response(success, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        # Actualización parcial de una Clasificación

        queryset = self.get_queryset(pk)
        if queryset:

            serializer = self.serializer_class(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            success = msg_success('Clasificación actualizada', 200)
            return Response(success, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        # Eliminación logica de una Clasificación

        classification = self.get_queryset(pk)
        if classification is not None:
            classification.state = False
            classification.save()

            success = msg_success('Clasificación eliminada', 200)
            return Response(success, status=status.HTTP_200_OK)
