from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Actualmente solo necesitamos esta View para crear Eventos
urlpatterns = [
    path("cities/", CityView.as_view(), name="cities"),
    path("", UbicacionCreateView.as_view(), name="guardar_ubicacion"),

]
