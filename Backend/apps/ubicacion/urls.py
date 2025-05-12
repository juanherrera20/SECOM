from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListarCityViewSet, CityView, UbicacionCreateView

#Router para manejar las rutas de los ViewSets
router = DefaultRouter()
router.register(r'lista_city', ListarCityViewSet)

# Actualmente solo necesitamos esta View para crear Eventos
urlpatterns = [
    path("municipios/", CityView.as_view(), name="municipios"),
    path("", UbicacionCreateView.as_view(), name="guardar_ubicacion"),

    path("", include(router.urls)),
]
