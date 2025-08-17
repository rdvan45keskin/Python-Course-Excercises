from django.urls import path
from . import views


urlpatterns = [
    #127.0.0.1:8000/login
    path("login/", views.login, name="login"),
    #127.0.0.1:8000/movies/2
    path("register/", views.register, name="register"),
    #127.0.0.1:8000/movies/search
    path("logout/", views.logout, name="logout"),
]
