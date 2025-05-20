from apps.ubicacion.serializers import CitySerializer
from apps.ubicacion.models import Departamento, City

def test_city_serializer():
    depto = Departamento(name="Atlantico")
    city = City(name="Barranquilla", departamento=depto, latitude=10.96, longitude=-74.8)
    serializer = CitySerializer(city)
    assert serializer.data["name"] == "Barranquilla"
