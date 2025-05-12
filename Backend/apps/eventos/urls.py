from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

#Router para manejar las rutas de los ViewSets
router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'posts', EventPostViewSet)


urlpatterns = [
    path('', include(router.urls)),  # Incluimos las rutas del router
    path('donaciones/', DonationView.as_view(), name='donaciones'),
    path('imagenes/<int:pk>/', ImageView.as_view(), name='imagenes'), # Ruta para las imagenes, necesita ID del evento

]
