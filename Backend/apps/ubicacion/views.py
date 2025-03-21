# Importamos Dependencias
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

# Importamos los modelos y serializadores necesarios
from .models import Ubicacion, Municipio, Departamento
from .serializers import UbicacionSerializer, MunicipioSerializer, Departamento


# Generics Permite manejar las peticiones CRUD de una vista en una sola clase
class MunicipioView(generics.ListAPIView):
    queryset = Municipio.objects.all()  # Obtener las instancias de la base de datos
    serializer_class = MunicipioSerializer
    permission_classes = [AllowAny]  # Cualquier usuario puede acceder


class UbicacionCreateView(generics.CreateAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
