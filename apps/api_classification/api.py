# Modulos nativos rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Modulo de python
from datetime import datetime

# Modulos Locales
from .serializers import ClassificationSerializer
from apps.metodosExternos import msg_error, resource_created, resource_updated, resource_destroy, not_found
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

        return Response(resource_created(), status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        # Actualización parcial de una Clasificación

        queryset = self.get_queryset(pk)
        if queryset:

            serializer = self.serializer_class(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(resource_updated(), status=status.HTTP_200_OK)
        return Response(not_found(), status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        # Eliminación logica de una Clasificación

        classification = self.get_queryset(pk)
        if classification is not None:

            classification.state = False
            classification.save()

            return Response(resource_destroy(), status=status.HTTP_200_OK)
        return Response(not_found(), status=status.HTTP_404_NOT_FOUND)
