from django.urls import path
from .api import *

urlpatterns = [
    path('api/', ClassificationAPI.as_view(), name='create'),
    path('api/<int:pk>', ClassificationDetailAPI.as_view(), name='detail'),
]
