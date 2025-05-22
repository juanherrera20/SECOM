from django.core.exceptions import ObjectDoesNotExist

from .models import Ubicacion, City
from rest_framework import serializers

class UbicacionService:
    @staticmethod
    def create(data):
        city_id = data.pop("city_id", None)
        lat = data.get("latitude", None)
        lng = data.get("longitude", None)

        if not city_id and (lat is None or lng is None):
            raise serializers.ValidationError("Debes enviar un city_id o lat/lng.")

        city = None
        if city_id:
            try:
                city = City.objects.get(id=city_id)
            except City.DoesNotExist:
                raise serializers.ValidationError("La ciudad especificada no existe.")

        return Ubicacion.objects.create(city=city, **data)
    
    @staticmethod
    def update(instance, data):
        city_id = data.pop("city_id", None)
        lat = data.get("latitude")
        lng = data.get("longitude")

        if not city_id and (lat is None or lng is None):
            raise serializers.ValidationError("Debes enviar un city_id o lat/lng.")

        if city_id:
            try:
                city = City.objects.get(id=city_id)
                instance.city = city
            except City.DoesNotExist:
                raise serializers.ValidationError("La ciudad especificada no existe.")

        for attr, value in data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

