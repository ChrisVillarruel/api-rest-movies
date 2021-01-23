from django.urls import path
from .api import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('api/<int:pk>', ClassificationDetailAPI.as_view(), name='detail'),
]
