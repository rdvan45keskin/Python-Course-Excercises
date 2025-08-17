from django.urls import path
from . import views


urlpatterns = [
    #127.0.0.1:8000/movies
    path("", views.index, name="movies"),
    #127.0.0.1:8000/movies/2
    path("<int:movie_id>", views.detail, name="detail"),
    #127.0.0.1:8000/movies/search
    path("search", views.search, name="search"),
]
