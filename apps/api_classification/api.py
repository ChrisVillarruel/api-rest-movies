from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from .models import Classification
from .serializers import ClassificationSerializer, ClassificationDetailSerializer


def msg_error(error, detail=None):
    msg_error = {
        'error': error,
        'detail': detail,
        'date': datetime.now().strftime("%A, %d. %B %Y %I:%M %p")
    }
    return msg_error

class ClassificationAPI(APIView):

    # list Classification
    def get(self, request):
        query_set = Classification.objects.all().values('classification_id', 'classification_name')
        serializers = ClassificationSerializer(instance=query_set, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    # create Classification
    def post(self, request):
        serializer = ClassificationSerializer(data=request.data)

        """ validaciones """
        if serializer.is_valid():
            classification_instance = serializer.save()
            msg_success = {
                'success': f'Clasificación {classification_instance.classification_name} creada'
            }
            return Response(msg_success, status=status.HTTP_201_CREATED)

        """ Error de validaciones """
        error = msg_error('Error de validación', serializer.errors)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class ClassificationDetailAPI(APIView):

    # get all Classification
    def get_query(self, pk=None):
        query_set = Classification.objects.filter(pk=pk).first()
        return query_set

    # detail Classification
    def get(self, request, pk=None):
        query_set = self.get_query(pk)

        if query_set is not None:
            serializer = ClassificationDetailSerializer(query_set)
            return Response(serializer.data, status=status.HTTP_200_OK)

        error = msg_error('La Clasificación que usted ingreso no existe')
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    # update Classification
    def put(self, request, pk=None):
        query_set = self.get_query(pk)

        if query_set is not None:
            serializer = ClassificationSerializer(instance=query_set, data=request.data)

            # validamos serializador
            if serializer.is_valid():
                classification_instance = serializer.save()
                msg_success = {
                    'success': f'Clasificación {classification_instance.classification_name} actualizada'
                }
                return Response(msg_success, status=status.HTTP_200_OK)

            # Error de validación
            error = msg_error('Error de validación', serializer.errors)
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        error = msg_error('La Clasificación que usted ingreso no existe')
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    # delete Classification
    def delete(self, request, pk=None):
        query_set = self.get_query(pk)

        if query_set is not None:
            query_set.delete()
            msg_success = {'success': f'Clasificación {query_set.classification_name} eliminada'}
            return Response(msg_success, status=status.HTTP_200_OK)

        error = msg_error('La Clasificación que ha ingresado no existe')
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
