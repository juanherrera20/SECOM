from rest_framework import serializers
from .models import Ubicacion, Departamento, Municipio


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"


class MunicipioSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()  # Incluye información del departamento

    class Meta:
        model = Municipio
        fields = "__all__"


class UbicacionSerializer(serializers.ModelSerializer):
    municipio = serializers.StringRelatedField()  # Solo muestra el nombre del municipio
    departamento = serializers.CharField(
        source="municipio.departamento.nombre", read_only=True
    )
    municipio_id = serializers.IntegerField(write_only=True)
    pais = serializers.CharField()
    ciudad = serializers.CharField()

    class Meta:
        model = Ubicacion
        fields = "__all__"
        # extra_kwargs = {'direccion': {'required': False}} #No es necesario que la dirección sea requerida
