
# Modulos nativos de rest_framework
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

# Modulos locales
from apps.metodosExternos import msg_error, resource_created, resource_updated, resource_destroy, not_found
from .serializers import MoviesSerializer
from .models import Movies


# class MoviesAPI(APIView):

#     def get(self, request):
#         query_set = Movies.objects.all()
#         serializers = MoviesSerializer(instance=query_set, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = MoviesSerializer(data=request.data)

#         if serializer.is_valid():
#             movies_instance = serializer.save()
#             msg_success = {
#                 'success': f'La Pelicula {movies_instance.name_movie} fue creada exitosamente'}
#             return Response(msg_success, status=status.HTTP_201_CREATED)

#         error = msg_error('Error de validación', 'BAD_REQUEST', 400, serializer.errors)
#         return Response(error, status=status.HTTP_400_BAD_REQUEST)


# class MoviesDetailAPI(APIView):

#     def get_query(self, pk=None):
#         query_set = Movies.objects.filter(pk=pk).first()
#         return query_set

#     # detail movie
#     def get(self, request, pk=None):
#         query_set = self.get_query(pk)

#         if query_set is not None:
#             serializer = MoviesDetailSerializer(instance=query_set)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         error = msg_error('Pelicula no encontrada', 'NOT_FOUND', 404)
#         return Response(error, status=status.HTTP_404_NOT_FOUND)

#     # update
#     def put(self, request, pk=None):
#         query_set = self.get_query(pk)

#         if query_set is not None:
#             serializer = MoviesSerializer(instance=query_set, data=request.data)

#             # validaciones
#             if serializer.is_valid():
#                 movies_instance = serializer.save()
#                 msg_success = {
#                     'success': f'La Pelicula {movies_instance.name_movie} fue actualizada exitosamente'}
#                 return Response(msg_success, status=status.HTTP_200_OK)

#             # error de validaciones
#             error = msg_error('Error de validación', 'BAD_REQUEST', 400, serializer.errors)
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)

#         error = msg_error('Pelicula no encontrada', 'NOT_FOUND', 404)
#         return Response(error, status=status.HTTP_404_NOT_FOUND)

#     # partial update
#     def patch(self, request, pk=None):
#         query_set = self.get_query(pk)

#         if query_set is not None:
#             serializer = MoviesSerializer(instance=query_set, data=request.data, partial=True)

#             # validaciones
#             if serializer.is_valid():
#                 movies_instance = serializer.save()
#                 msg_success = {
#                     'success': f' La Pelicula {movies_instance.name_movie} fue actualizada exitosamente'}
#                 return Response(msg_success, status=status.HTTP_200_OK)

#             # error de validaciones
#             error = msg_error('Error de validación', 'BAD_REQUEST', 400, serializer.errors)
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)

#         error = msg_error('Pelicula no encontrada', 'NOT_FOUND', 404)
#         return Response(error, status=status.HTTP_404_NOT_FOUND)

#     # delete
#     def delete(self, request, pk=None):
#         query_set = self.get_query(pk)

#         if query_set is not None:
#             query_set.delete()
#             msg_success = {
#                 'success': f'La Pelicula {query_set.name_movie} fue eliminada exitosamente'}
#             return Response(msg_success, status=status.HTTP_200_OK)

#         error = msg_error('Pelicula no encontrada', 'NOT_FOUND', 404)
#         return Response(error, status=status.HTTP_404_NOT_FOUND)


class MoviesViewSet(ModelViewSet):
    serializer_class = MoviesSerializer

    def get_queryset(self, pk=None):
        # Si pk es None, retornamos un listado. De lo contrario retornamos un objeto

        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)

        return self.get_serializer().Meta.model.objects.filter(movie_id=pk, state=True).first()

    def create(self, request):
        # Metodo encargado de crear una pelicula

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(resource_created(), status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        # Metodo encargado de actualizar una pelicula

        queryset = self.get_queryset(pk)
        if queryset:
            serializer = self.serializer_class(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(resource_updated(), status=status.HTTP_200_OK)
        return Response(not_found(), status=status.HTTP_404_NOT_FOUND)
