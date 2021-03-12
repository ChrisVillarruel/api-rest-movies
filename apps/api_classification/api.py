# Modulos nativos rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Modulo de python
from datetime import datetime

# Modulos Locales
from .serializers import ClassificationSerializer, ClassificationDetailSerializer
from apps.metodosExternos import msg_error
from .models import Classification

class ClassificationAPI(APIView):

    def get(self, request):
        query_set = Classification.objects.all().values('classification_id', 'classification_name', 'classification_desc')
        serializers = ClassificationSerializer(instance=query_set, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClassificationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            msg_success = {'success': 'Clasificación creada exitosamente'}
            return Response(msg_success, status=status.HTTP_201_CREATED)

        error = msg_error('Error de validación', 'BAD_REQUEST', 400, serializer.errors)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

class ClassificationDetailAPI(APIView):

    def get_query(self, pk=None):
        query_set = Classification.objects.filter(pk=pk).first()
        return query_set

    def get(self, request, pk=None):
        query_set = self.get_query(pk)

        if query_set is not None:
            serializer = ClassificationDetailSerializer(query_set)
            return Response(serializer.data, status=status.HTTP_200_OK)

        error = msg_error('Clasificación no encontrada', 'NOT_FOUND', 404)
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        query_set = self.get_query(pk)

        if query_set is not None:
            serializer = ClassificationSerializer(instance=query_set, data=request.data)

            if serializer.is_valid():
                classification_instance = serializer.save()
                msg_success = {'success': 'Clasificación actualizada exitosamente'}
                return Response(msg_success, status=status.HTTP_200_OK)

            error = msg_error('Error de validación', 'BAD_REQUEST', 400, serializer.errors)
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        error = msg_error('Clasificación no encontrada', 'NOT_FOUND', 404)
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    # delete Classification
    def delete(self, request, pk=None):
        query_set = self.get_query(pk)

        if query_set is not None:
            query_set.delete()
            msg_success = {'success': f'Clasificación eliminada exitosamente'}
            return Response(msg_success, status=status.HTTP_200_OK)

        error = msg_error('Clasificación no encontrada', 'NOT_FOUND', 404)
        return Response(error, status=status.HTTP_404_NOT_FOUND)
