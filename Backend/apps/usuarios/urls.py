from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSets

# Crear un router
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSets)

# Incluir las rutas del router
urlpatterns = [
    path('', include(router.urls)),
]