# Modulos nativos de rest_framework
from rest_framework.routers import DefaultRouter

# Modulos locales
from .api import MoviesViewSet


routers = DefaultRouter()
routers.register('', MoviesViewSet, basename='movies')
urlpatterns = routers.urls
