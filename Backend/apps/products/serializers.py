from django.conf import settings
from django.db import transaction

from rest_framework import serializers

from .models import Product, Offer, Category, Tag  # Asegúrate de que el modelo esté definido correctamente

class OfferSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Offer
        fields = ['id', 'offer_price', 'active', 'discount_percentage']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  
        fields = '__all__'  # Esto incluirá todos los campos del modelo
        
         
class ProductListSerializer(serializers.ModelSerializer):
    offer = OfferSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    # is_wishilist = serializers.SerializerMethodField() Revisar si es necesario Agregar campo para saber si el producto esta en la wishlist del usuario
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'offer', 'rating', 'tags', 'image']
    
    #To get the Product's Principal Image 
    def get_image(self, obj):
        request = self.context.get('request')
        image = obj.images.order_by('order').first()
        if image and image.url:
            return request.build_absolute_uri(image.url.url) if request else f"{settings.MEDIA_URL}{image.url}"
        return None  
    
    def get_rating(self, obj):
        user = obj.user
        print(f"user: {user}") 
        if user.reputacion:
            return user.reputacion
        else:
            return None
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
    