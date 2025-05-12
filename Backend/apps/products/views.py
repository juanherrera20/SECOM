from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .serializers import ProductSerializer  # Asegúrate de que el serializer esté definido correctamente
from .models import Product  # Asegúrate de que el modelo esté definido correctamente

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer  # Define el serializador que usarás para validar los datos de entrada
    queryset = Product.objects.all() 
    permission_classes = [permissions.AllowAny]  