from rest_framework import serializers
from .models import Departamento, City, Ubicacion

# Serializador para Departamento
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['id', 'name']


# Serializador para Ciudad (antes Municipio)
class CitySerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()

    class Meta:
        model = City
        fields = ['id', 'name', 'departamento', 'latitude', 'longitude']


# Serializador para Ubicación
class UbicacionSerializer(serializers.ModelSerializer):
    # Relación de ciudad, usando PrimaryKeyRelatedField, ya que ahora usamos City
    city = CitySerializer(read_only=True)
    city_id = serializers.IntegerField(write_only=True)  # Campo para asociar la ciudad por ID
    pais = serializers.CharField(required=False)

    class Meta:
        model = Ubicacion
        fields = ['id', 'name', 'city', 'city_id', 'address', 'latitude', 'longitude', 'pais']
