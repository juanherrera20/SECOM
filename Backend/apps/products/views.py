from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ProductSerializer, ProductListSerializer, CategorySerializer, TagSerializer  # Asegúrate de que el serializer esté definido correctamente
from .models import Product, Category, Tag  # Asegúrate de que el modelo esté definido correctamente

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
    
    
#View to list the categories
class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #only can Read info
    serializer_class = CategorySerializer

    
class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #only can Read info
    serializer_class = TagSerializer
    #Filtering
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
