from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classifications/', include('apps.api_classification.routers')),
    path('categories/', include('apps.api_movie_category.urls')),
    path('movies/', include('apps.api_movies.urls')),
]
