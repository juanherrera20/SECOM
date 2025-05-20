from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from django.db import transaction
from django.conf import settings

from apps.ubicacion.serializers import UbicacionSerializer
from apps.ubicacion.models import City, Ubicacion
from apps.usuarios.models import CustomUser
from .models import Evento, Image, Donation, EventPost

# Serializador para crear y actualizar eventos
class EventoSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()
    type_donation = serializers.StringRelatedField()
    organizador = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=False)
    donation_id = serializers.IntegerField(write_only=True)
    #meet_date = serializers.DateField(required=False, allow_null=True)
    
    class Meta:
        model = Evento
        fields = '__all__'
        extra_kwargs = {'meet_date': {'allow_null': True}} # Similar to the original code, allowing null values

    def create(self, validated_data):
        ubicacion_data = validated_data.pop("ubicacion", None)
        donation_id = validated_data.pop('donation_id', None)

        try:
            with transaction.atomic():
                ubicacion = None
                if ubicacion_data:
                    city_id = ubicacion_data.pop("city_id", None)

                    if city_id is None and (ubicacion_data.get("latitude") is None or ubicacion_data.get("longitude") is None):
                        raise serializers.ValidationError("Provide location data: either a city_id or both latitude and longitude.")

                    city = None
                    if city_id:
                        try:
                            city = City.objects.get(id=city_id)
                        except ObjectDoesNotExist:
                            raise serializers.ValidationError("City with the given ID does not exist.")
                    
                    ubicacion = Ubicacion.objects.create(city=city, **ubicacion_data)

                if donation_id:
                    try:
                        donation = Donation.objects.get(id=donation_id)
                    except Donation.DoesNotExist:
                        raise serializers.ValidationError("Donation with the given ID does not exist.")
                else:
                    donation = Donation.objects.get(name="Cualquiera")

                evento = Evento.objects.create(ubicacion=ubicacion, type_donation=donation, **validated_data)

            return evento

        except Exception as e:
            raise serializers.ValidationError(f"Error during the event creation: {str(e)}")


    def update(self, instance, validated_data):
        ubicacion_data = validated_data.pop("ubicacion", None)
        donation_id = validated_data.pop('donation_id', None)

        try:
            with transaction.atomic():
                if ubicacion_data:
                    city_id = ubicacion_data.pop("city_id", None)

                    # Validación similar a la usada en 'create'
                    lat = ubicacion_data.get("latitude")
                    lng = ubicacion_data.get("longitude")
                    if not city_id and (lat is None or lng is None):
                        raise serializers.ValidationError("Debe proporcionar una ciudad o coordenadas válidas para la ubicación.")

                    # Cambiar ciudad si es distinta
                    if city_id and (not instance.ubicacion.city or city_id != instance.ubicacion.city.id):
                        try:
                            city = City.objects.get(id=city_id)
                            instance.ubicacion.city = city
                        except City.DoesNotExist:
                            raise serializers.ValidationError("La ciudad especificada no existe.")

                    # Actualizar otros campos de ubicación
                    for attr, value in ubicacion_data.items():
                        setattr(instance.ubicacion, attr, value)
                    instance.ubicacion.save()

                # Actualizar donación si es distinta
                if donation_id and (not instance.type_donation or donation_id != instance.type_donation.id):
                    try:
                        donacion = Donation.objects.get(id=donation_id)
                        instance.type_donation = donacion
                    except Donation.DoesNotExist:
                        raise serializers.ValidationError("La donación especificada no existe.")

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
