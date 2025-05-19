from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

#Router para manejar las rutas de los ViewSets
router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'posts', EventPostViewSet)


urlpatterns = [
    path('', include(router.urls)),  # Incluimos las rutas del router
    path('donations/', DonationView.as_view(), name='donations'),
    path('donations/evento/<int:evento_id>/', get_donacion_por_evento, name='donacion-por-evento'),
    path('images/<int:pk>/', ImageView.as_view(), name='images'), # Ruta para las imagenes, necesita ID del evento

]
