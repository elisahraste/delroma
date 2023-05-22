from django.urls import path
from . import views


urlpatterns = [
    path("", views.nuevousuario),
    path("registrarse/<str: email>", views.registarse),
]