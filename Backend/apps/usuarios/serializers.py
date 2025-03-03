from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Solo para escritura, no se devolverá en la respuesta

    class Meta: 
        model = CustomUser
        fields = '__all__'

    # Sobreescribimos el método `create` para los usuarios (CustomUser)
    def create(self, validated_data):
        print("Esta en el metodo create")
        first_name = validated_data["first_name"]
        print(f"Primer nombre: {first_name}")
        username = first_name.replace(" ", "")  # Quito los espacios
        print(f"Nombre de usuario: {username}")

        # Se crea el usuario con `set_password` para que la contraseña se almacene correctamente
        user = CustomUser(username=username, **validated_data)
        user.set_password(validated_data["password"])  # Hash de la contraseña
        user.save()

        return user
