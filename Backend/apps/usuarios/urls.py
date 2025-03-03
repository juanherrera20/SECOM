"""Aquí se crean las rutas de acceso para la apliación de Usuarios,
    Se encargará de la autenticación y el manejo de usuarios"""

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CustomTokenObtainPairView, CustomRefreshTokenView #Autenticación
from .views import ( #Vistas de la aplicación
    register, logout, CustomUserView
    )

urlpatterns = [
    #Vista protegida para pruebas
    path("restringedView/", views.restringedView, name="index"),
    
    path("register/",register.as_view(), name="register"),
    path("me/", CustomUserView.as_view(), name="user"),
    
    # Ruta de cierre de sesión
    path("logout/", logout, name="logout"),
    
     #Rutas para el manejo de tokens
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),
]