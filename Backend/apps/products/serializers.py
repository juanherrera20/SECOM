
#Todo esto es provisional
from rest_framework import serializers
from .models import Product  # Asegúrate de que el modelo esté definido correctamente

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # Asegúrate de que el modelo esté definido correctamente
        fields = '__all__'  # Esto incluirá todos los campos del modelo