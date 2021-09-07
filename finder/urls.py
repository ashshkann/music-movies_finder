from django.urls import path
from .views import home, music, music_views, movies, movies_views

urlpatterns = [
    path('', home, name='homepage'),
    path('music', music, name='musicpage'),
    path('music-result', music_views),
    path('movies', movies, name="moviespage"),
    path('movies-result', movies_views),
]
