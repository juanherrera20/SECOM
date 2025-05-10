from rest_framework import serializers
from django.db import transaction
from django.conf import settings

from apps.ubicacion.serializers import UbicacionSerializer
from apps.ubicacion.models import City, Ubicacion
from apps.usuarios.models import CustomUser
from .models import Evento, Image, Donation

# Serializador para crear y actualizar eventos
class EventoSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()
    donation = serializers.StringRelatedField()
    organizador = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=False)
    donation_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Evento
        fields = '__all__'

    def create(self, validated_data):
        ubicacion_data = validated_data.pop("ubicacion", None)
        donacion_id = validated_data.pop('donation_id', None)
        
        try:
            with transaction.atomic():
                if ubicacion_data:
                    city_id = ubicacion_data.pop("city_id")
                    city = City.objects.get(id=city_id)
                    
                    ubicacion = Ubicacion.objects.create(city=city, **ubicacion_data)

                if donacion_id:
                    donacion = Donation.objects.get(id=donacion_id)
                else:
                    donacion = Donation.objects.get(name="Cualquiera")

                evento = Evento.objects.create(ubicacion=ubicacion, type_donation=donacion, **validated_data)
            
            return evento
        
        except Exception as e:
            raise serializers.ValidationError(f"Error during the event creation: {str(e)}")

    def update(self, instance, validated_data):
        ubicacion_data = validated_data.pop("ubicacion", None)
        donacion_id = validated_data.pop('donation_id', None)

        try:
            with transaction.atomic():
                if ubicacion_data:
                    city_id = ubicacion_data.pop("city_id", None)
                    if city_id and city_id != instance.ubicacion.city.id:
                        city = City.objects.get(id=city_id)
                        instance.ubicacion.city = city

                    for attr, value in ubicacion_data.items():
                        setattr(instance.ubicacion, attr, value)

                    instance.ubicacion.save()

                if donacion_id and donacion_id != instance.type_donation.id:
                    donacion = Donation.objects.get(id=donacion_id)
                    instance.type_donation = donacion

                for attr, value in validated_data.items():
                    setattr(instance, attr, value)

                instance.save()

            return instance

        except Exception as e:
            raise serializers.ValidationError(f"Error during the event update: {str(e)}")


# Serializador para listar eventos resumidos
class EventoListSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()
    image = serializers.SerializerMethodField()

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
