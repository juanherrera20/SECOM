import pytest
from apps.ubicacion.models import Departamento, City, Ubicacion

@pytest.mark.django_db
def test_departamento_str():
    depto = Departamento.objects.create(name="Antioquia")
    assert str(depto) == "Antioquia"

@pytest.mark.django_db
def test_city_str():
    depto = Departamento.objects.create(name="Cundinamarca")
    city = City.objects.create(name="Bogotá", departamento=depto, latitude=4.60971, longitude=-74.08175)
    assert str(city) == "Bogotá"

@pytest.mark.django_db
def test_ubicacion_str():
    depto = Departamento.objects.create(name="Valle del Cauca")
    city = City.objects.create(name="Cali", departamento=depto, latitude=3.45, longitude=-76.52)
    ubicacion = Ubicacion.objects.create(name="Plaza Caicedo", city=city, address="Centro", pais="Colombia")
    assert str(ubicacion) == "Plaza Caicedo, Cali"
