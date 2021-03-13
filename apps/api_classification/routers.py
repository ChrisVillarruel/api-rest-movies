from rest_framework.routers import DefaultRouter

from apps.api_classification.api import ClassificationViewSet


routers = DefaultRouter()
routers.register('', ClassificationViewSet, basename='classifications')
urlpatterns = routers.urls
