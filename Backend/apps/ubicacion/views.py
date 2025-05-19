# Importamos Dependencias
from rest_framework import generics, status, serializers, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

# Importamos los modelos y serializadores necesarios
from .models import Ubicacion, City, Departamento
from .serializers import UbicacionSerializer, CitySerializer, DepartamentoSerializer


# View para manejar las ciudades (anteriormente municipios)
class CityView(generics.ListAPIView):
    queryset = City.objects.all()  # Obtener las instancias de la base de datos
    serializer_class = CitySerializer
    permission_classes = [AllowAny]  # Cualquier usuario puede acceder


# View para listar por ID
class CityDetailView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [AllowAny]


# View para crear una ubicación
class UbicacionCreateView(generics.CreateAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def perform_create(self, serializer):
        city_id = self.request.data.get('city_id')  # Obtener el city_id del request
        try:
            city = City.objects.get(id=city_id)  # Verificar si la ciudad existe
            serializer.save(city=city, usuario=self.request.user)  # Guardar la ubicación con la ciudad seleccionada
        except City.DoesNotExist:
            raise serializers.ValidationError("La ciudad seleccionada no existe.")
