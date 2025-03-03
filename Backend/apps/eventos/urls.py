from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, ImagenView, DonacionView

#Router para manejar las rutas de los ViewSets
router = DefaultRouter()
router.register(r'eventos', EventoViewSet)


urlpatterns = [
    path('', include(router.urls)),  # Incluimos las rutas del router
    path('donaciones/', DonacionView.as_view(), name='donaciones'),
    path('imagenes/<int:pk>/', ImagenView.as_view(), name='imagenes'), # Ruta para las imagenes, necesita ID del evento
]
