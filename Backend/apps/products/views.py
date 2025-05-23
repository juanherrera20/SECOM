from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import (
    ProductSerializer, ProductListSerializer, CategorySerializer, 
    TagSerializer, ImageSerializer, OfferSerializer
)  
from .models import Product, Category, Tag, Image, Offer, WishList, State
from .filters import ProductFilter  # Import Filters

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = (
        Product.objects.all()
        .select_related('user', 'category', 'ubicacion')
        .prefetch_related('tags', 'offer', 'wishlist', 'images')
    )
    permission_classes = [permissions.AllowAny]
    
    #Custom Filtering
    filterset_class = ProductFilter 
    #Searching
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    #ordering
    ordering_fields = ["price", "user__reputacion", "create_date"]
    
    #define serializer to use according to request
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer
    
    # Extra petition to Add product to the wishList
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def add_favorites(self, request, pk=None):
        user = request.user
        try:
            product = self.get_object()
            wishlist_item, created = WishList.objects.get_or_create(user=user, product=product)
            
            if not created:
                return Response(
                    {"detail": "Product is already in wishlist."},
                    status=status.HTTP_200_OK
                )
            
            return Response(
                {"detail": "Product added to wishlist successfully."},
                status=status.HTTP_201_CREATED
            )
        except Product.DoesNotExist:
            return Response(
                {"detail": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        

#Views for Offers Instances
class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.select_related('product')
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]
    serializer_class = OfferSerializer
    #Filtering
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active']
    
    
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


# Vista para manejar imágenes del evento (GET y POST)
class ImageView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        try:
            images = Image.objects.filter(product_id=pk).order_by("order")
            serializer = ImageSerializer(images, many=True, context={'request': request})
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": " Product no encontrado"}, status=404)

    def post(self, request, pk, format=None):
        new_images = request.FILES.getlist("new_images", [])
        deleted_images = request.data.getlist("deleted_images", [])

        try:
            product = Product.objects.prefetch_related('images').get(id=pk)
        except Product.DoesNotExist:
            return Response({"error": "Evento no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        images = product.images.all()

        # Eliminar imágenes marcadas
        for image_id in deleted_images:
            try:
                obj = images.get(id=image_id)
                obj.delete()
                images = images.exclude(id=image_id)
            except Image.DoesNotExist:
                continue

        # Reordenar existentes
        for index, image in enumerate(images.order_by("order"), start=1):
            image.order = index
            image.save(update_fields=["order"])

        # Agregar nuevas
        next_order = images.count() + 1
        for img in new_images:
            Image.objects.create(url=img, product=product, order=next_order)
            next_order += 1

        return Response(status=status.HTTP_204_NO_CONTENT)


#------------------ List Choices Options -----------------------------
# Listar los Estados de un Producto para los inputs Select
class StateView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #permissions.IsAdminUser
    
    def get(self, request):
        states_choices = [{'value': choice[0], 'label': choice[1]} for choice in State.choices] 

        return Response(
            states_choices  
        )
        
# Listar los Estados de un Producto para los inputs Select
class ConditionView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #permissions.IsAdminUser
    
    def get(self, request):
        conditions_choices = [{'value': choice[0], 'label': choice[1]} for choice in Product.Condition.choices] 

        return Response(
            conditions_choices
        )
        
