from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from django.db import transaction
from django.conf import settings

from apps.ubicacion.serializers import UbicacionSerializer
from apps.ubicacion.models import City
from apps.ubicacion.utils import UbicacionService #Import Class to create and update Ubicacion instance
from apps.usuarios.models import CustomUser
from .models import Evento, Image, Donation, EventPost

# Serializador para crear y actualizar eventos
class EventoSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()
    type_donation = serializers.StringRelatedField(read_only=True)
    donation_id = serializers.PrimaryKeyRelatedField(queryset=Donation.objects.all(), source='type_donation')
    organizador = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=False)
    #meet_date = serializers.DateField(required=False, allow_null=True)
    
    class Meta:
        model = Evento
        fields = '__all__'
        extra_kwargs = {'meet_date': {'allow_null': True}} # Similar to the original code, allowing null values
    
    def create(self, validated_data):
        ubicacion_data = validated_data.pop("ubicacion", None)

        try:
            with transaction.atomic():
                ubicacion = None
                if ubicacion_data:
                    ubicacion = UbicacionService.create(ubicacion_data)

                evento = Evento.objects.create(ubicacion=ubicacion, **validated_data)

            return evento

        except Exception as e:
            raise serializers.ValidationError(f"Error durante la creación del evento: {str(e)}")
    
    def update(self, instance, validated_data):
        ubicacion_data = validated_data.pop("ubicacion", None)

        try:
            with transaction.atomic():
                if ubicacion_data:
                    UbicacionService.update(instance.ubicacion, ubicacion_data)

                # Actualizar campos del evento
                for attr, value in validated_data.items():
                    setattr(instance, attr, value)
                instance.save()

            return instance

        except Exception as e:
            raise serializers.ValidationError(f"Error durante la actualización del evento: {str(e)}")

 
# Serializador para listar eventos resumidos
class EventoListSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()
    image = serializers.SerializerMethodField()
    type_donation = serializers.StringRelatedField()

    class Meta:
        model = Evento
        fields = ['id', 'name', 'meet_date', 'type_donation', 'ubicacion', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        image = obj.images.order_by('order').first()
        if image and image.url:
            return request.build_absolute_uri(image.url.url) if request else f"{settings.MEDIA_URL}{image.url}"
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


# Serializador para tipos de donaciones
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'name']
        

# Serializador para los posts de eventos
class EventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPost
        fields = ['id', 'content', 'create_date', 'evento']
