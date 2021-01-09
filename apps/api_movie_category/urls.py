from django.urls import path
from .api import *

urlpatterns = [
    path('api/', CategoryMoviesAPI.as_view(), name='list'),
    path('api/<int:pk>', CategoryMoviesDetailAPI.as_view(), name='detail'),
]
