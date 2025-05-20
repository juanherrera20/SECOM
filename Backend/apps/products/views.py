from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

from .serializers import ProductSerializer, ProductListSerializer, CategorySerializer  # Asegúrate de que el serializer esté definido correctamente
from .models import Product, Category  # Asegúrate de que el modelo esté definido correctamente

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = (
        Product.objects.all()
        .select_related('user', 'category', 'ubicacion')
        .prefetch_related('tags', 'offer', 'wishlist', 'images')
    )
    permission_classes = [permissions.AllowAny]
    
    #define serializer to use according to request
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer
    
class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #only can Read info
    serializer_class = CategorySerializer
    