from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MunicipioView, UbicacionCreateView

# Actualmente solo necesitamos esta View para crear Eventos
urlpatterns = [
    path("municipios/", MunicipioView.as_view(), name="municipios"),
    path("", UbicacionCreateView.as_view(), name="guardar_ubicacion"),
]
