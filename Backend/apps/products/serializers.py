from django.conf import settings
from django.db import transaction
from django.utils import timezone

from rest_framework import serializers

from .models import Product, Offer, Category, Tag, Image  # Asegúrate de que el modelo esté definido correctamente

from apps.usuarios.serializers import CustomUserSerializer
from apps.usuarios.models import CustomUser
from apps.ubicacion.serializers import UbicacionSerializer
from apps.ubicacion.utils import UbicacionService

class OfferSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    class Meta: 
        model = Offer
        fields = [
            'id', 'offer_price', 'active', 
            'discount_percentage', 'start_date',
            'end_date', 'product',
        ]
        extra_kwargs = {
            'end_date': {'allow_null': True, 'required': False}, 
            'start_date': {'allow_null': True, 'required': False}, 
        }
        
    # Si llega None o null, lo convertimos al valor por default para el modelo
    def validate_start_date(self, value):
        if value is None:
            return timezone.now().date()
        return value


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    tags_ids = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), source='tags', many=True)
    user = CustomUserSerializer(read_only=True)
    # user_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='user', write_only=True)
    ubicacion = UbicacionSerializer()
    
    class Meta:
        model = Product  
        fields = [
            'id', 'name', 'description', 'category', 'category_id',
            'tags', 'tags_ids', 'user', 'ubicacion',
            'price', 'condition', 'state', 'create_date'
        ] 
        read_only_fields = ['create_date', 'state']
        extra_kwargs = {'price': {'allow_null': True, 'required': False}}
        
    def validate_price(self, value):
        # Si llega None o null, lo convertimos a 0 para el modelo
        if value is None:
            return 0
        return value
        
    def create(self, validated_data):
        ubicacion_data = validated_data.pop("ubicacion", None)
        tags = validated_data.pop("tags", [])

        try:
            with transaction.atomic():
                #Get User by Request, it's not necessary send User_id
                user = self.context['request'].user

                ubicacion = None
                if ubicacion_data:
                    ubicacion = UbicacionService.create(ubicacion_data)

                product = Product.objects.create(
                    ubicacion=ubicacion,
                    user=user,
                    **validated_data
                )
                product.tags.set(tags)

                return product

        except Exception as e:
            raise serializers.ValidationError(f"Error during the product creation: {str(e)}")
    
    def update(self, instance, validated_data):
        ubicacion_data = validated_data.pop("ubicacion", None)
        tags = validated_data.pop("tags", [])
        print(f"Estas son las tags {tags}")
        
        try: 
            with transaction.atomic():
                #Update Ubicación by method update ubication
                if ubicacion_data:
                    UbicacionService.update(instance.ubicacion, ubicacion_data)
                    
                #Update Tags
                instance.tags.set(tags)
                
                #update Instance (product)
                super().update(instance, validated_data)
                
            return instance
                    
        except Exception as e:
            raise serializers.ValidationError(f"Error during the product update: {str(e)}")
    
         
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
        if user.reputacion:
            return user.reputacion
        else:
            return None
        
# Serializador de imagenes
class ImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'url', 'order']

    def get_url(self, obj):
        request = self.context.get('request')
        if obj.url:
            return request.build_absolute_uri(obj.url.url) if request else f"{settings.MEDIA_URL}{obj.url}"
        return None


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name'] # category

    