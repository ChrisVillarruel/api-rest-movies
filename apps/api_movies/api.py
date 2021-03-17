
# Modulos nativos de rest_framework
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

# Modulos locales
from apps.metodosExternos import msg_error, resource_created, resource_updated, resource_destroy, not_found
from pagination import StandardResultsSetPagination
from .serializers import MoviesSerializer
from .models import Movies


class MoviesViewSet(ModelViewSet):
    serializer_class = MoviesSerializer
    pagination_class = StandardResultsSetPagination

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

    def destroy(self, request, pk=None):
        # Metodo encargado de eliminar de forma logica una pelicula

        queryset = self.get_queryset(pk)
        if queryset:
            queryset.state = False
            queryset.save()

            return Response(resource_destroy(), status=status.HTTP_200_OK)
        return Response(not_found(), status=status.HTTP_404_NOT_FOUND)
