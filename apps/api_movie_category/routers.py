# Modulos nativos de rest_framework
from rest_framework.routers import DefaultRouter

# Modulos locales
from .api import MovieCategoryViewSet


# Registramos una ruta
routers = DefaultRouter()
routers.register('', MovieCategoryViewSet, basename='category-movies')
urlpatterns = routers.urls
