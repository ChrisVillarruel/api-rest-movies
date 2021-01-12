from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from .models import Movies
from .serializers import MoviesSerializer, MoviesDetailSerializer

# mostrar error de validación


def msg_error(error, detail=None):
    if detail is None:
        detail = 'Sin descripción'

    msg_error = {
        'error': error,
        'detail': detail,
        'date': datetime.now().strftime("%A, %d. %B %Y %I:%M %p")
    }
    return msg_error


class MoviesAPI(APIView):

    def get(self, request):
        query_set = Movies.objects.all().values('movie_id', 'name_movie', 'launch_year')
        serializers = MoviesSerializer(instance=query_set, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MoviesSerializer(data=request.data)

        if serializer.is_valid():
            movies_instance = serializer.save()
            msg_success = {
                'success': f'La Pelicula {movies_instance.name_movie} creada exitosamente'}
            return Response(msg_success, status=status.HTTP_201_CREATED)

        error = msg_error('Error de Validación', serializer.errors)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class MoviesDetailAPI(APIView):

    def get_query(self, pk=None):
        query_set = Movies.objects.filter(pk=pk).first()
        return query_set

    # detail movie
    def get(self, request, pk=None):
        query_set = self.get_query(pk)

        if query_set is not None:
            serializer = MoviesDetailSerializer(instance=query_set)
            return Response(serializer.data, status=status.HTTP_200_OK)

        error = msg_error('Pelicula no encontrada')
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    # update
    def put(self, request, pk=None):
        query_set = self.get_query(pk)

        if query_set is not None:
            serializer = MoviesSerializer(instance=query_set, data=request.data)

            # validaciones
            if serializer.is_valid():
                movies_instance = serializer.save()
                msg_success = {
                    'success': f'La Pelicula {movies_instance.name_movie} fue actualizada exitosamente'}
                return Response(msg_success, status=status.HTTP_200_OK)

            # error de validaciones
            error = msg_error('Error de Validación', serializer.errors)
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        error = msg_error('Pelicula no encontrada')
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    # partial update
    def patch(self, request, pk=None):
        query_set = self.get_query(pk)

        if query_set is not None:
            serializer = MoviesSerializer(instance=query_set, data=request.data, partial=True)

            # validaciones
            if serializer.is_valid():
                movies_instance = serializer.save()
                msg_success = {
                    'success': f' La Pelicula {movies_instance.name_movie} fue actualizada exitosamente'}
                return Response(msg_success, status=status.HTTP_200_OK)

            # error de validaciones
            error = msg_error('Error de Validación', serializer.errors)
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        error = msg_error('Pelicula no encontrada')
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk=None):
        query_set = self.get_query(pk)

        if query_set is not None:
            query_set.delete()
            msg_success = {
                'success': f'La Pelicula {movies_instance.name_movie} fue eliminada exitosamente'}
            return Response(msg_success, status=status.HTTP_200_OK)

        error = msg_error('Pelicula no encontrada')
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
