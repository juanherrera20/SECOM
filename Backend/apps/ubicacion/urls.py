from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MunicipioView

#Actualmente solo necesitamos esta View para crear Eventos
urlpatterns = [
    path('municipios/', MunicipioView.as_view(), name='municipios'),
]
