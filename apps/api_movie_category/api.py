
# Modulos nativos de rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

# from .serializers import CategorySerializers
from apps.metodosExternos import msg_error, msg_success
from .serializers import MovieCategorySerializers
from .models import MovieCategory


# class CategoryMoviesAPI(APIView):

#     def get(self, request):
#         query_set = MovieCategory.objects.all()
#         serializers = CategorySerializers(instance=query_set, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)

#     # create
#     def post(self, request):
#         json_data = request.data
#         serializer = CategorySerializers(data=json_data)

#         # validaciones
#         if serializer.is_valid():
#             category_instance = serializer.save()
#             msg_success = {
#                 'success': f'La Categoria {category_instance.category_name} creada exitosamente'}
#             return Response(msg_success, status=status.HTTP_201_CREATED)

#         # error de validaciones
#         error = msg_error('Error de validación', 'BAD_REQUEST', 400, serializer.errors)
#         return Response(error, status=status.HTTP_400_BAD_REQUEST)


# class CategoryMoviesDetailAPI(APIView):

#     # Para evitar el uso de excepciones se creo este metodo
#     def get_query(self, pk=None):
#         query_set = MovieCategory.objects.filter(pk=pk).first()
#         return query_set

#     # detallar categoria
#     def get(self, request, pk=None):
#         query_set = self.get_query(pk)

#         if query_set is not None:
#             serializer = CategorySerializers(instance=query_set)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         error = msg_error('Categoria no encontrada', 'NOT_FOUND', 404)
#         return Response(error, status=status.HTTP_404_NOT_FOUND)

#     # actualizar categoria
#     def put(self, request, pk=None):
#         query_set = self.get_query(pk)

#         if query_set is not None:
#             serializer = CategorySerializers(instance=query_set, data=request.data)

#             # validaciones
#             if serializer.is_valid():
#                 category_instance = serializer.save()
#                 msg_success = {
#                     'success': f'La Categoria {category_instance.category_name} actualizada exitosamente'}
#                 return Response(msg_success, status=status.HTTP_200_OK)

#             # Error de validación
#             error = msg_error('Error de validación', 'BAD_REQUEST', 400, serializer.errors)
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)

#         # categoria no encontrada
#         error = msg_error('Categoria no encontrada', 'NOT_FOUND', 404)
#         return Response(error, status=status.HTTP_404_NOT_FOUND)

#     # eliminar Categoria
#     def delete(self, request, pk=None):
#         query_set = self.get_query(pk)

#         if query_set is not None:
#             query_set.delete()
#             msg_success = {
#                 'success': f'La Categoria {query_set.category_name} eliminada exitosamente'}
#             return Response(msg_success, status=status.HTTP_200_OK)

#         # categoria no encontrada
#         error = msg_error('Categoria no encontrada', 'NOT_FOUND', 404)
#         return Response(error, status=status.HTTP_404_NOT_FOUND)


class MovieCategoryViewSet(ModelViewSet):
    serializer_class = MovieCategorySerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)

        return self.get_serializer().Meta.model.objects.filter(category_id=pk, state=True).first()
