"""import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from django.urls import reverse
from rest_framework.test import APIClient
from apps.ubicacion.models import Departamento, City, Ubicacion
from apps.usuarios.models import CustomUser

@pytest.mark.django_db
def test_listar_cities():
    user = CustomUser.objects.create_user(username="testuser", email="user@test.com", password="test1234")
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)

    print(f"Token generado: {token}")  # Para depuración

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    depto = Departamento.objects.create(name="Cesar")
    City.objects.create(name="Valledupar", departamento=depto, latitude=10.47, longitude=-73.25)

    response = client.get(reverse("city-list"))
    print(response.status_code, response.json())  # Ver qué devuelve exactamente
    assert response.status_code == 200



@pytest.mark.django_db
def test_create_ubicacion():
    user = CustomUser.objects.create_user(username="testuser", email="test@example.com", password="pass1234")
    depto = Departamento.objects.create(name="Guajira")
    city = City.objects.create(name="Riohacha", departamento=depto, latitude=11.54, longitude=-72.91)

    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    print(f"Token generado: {token}")  # Para depuración

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    data = {
        "name": "Centro Cultural",
        "address": "Calle 10",
        "city_id": city.id,
        "latitude": 11.54,
        "longitude": -72.91,
        "pais": "Colombia"
    }

    response = client.post(reverse("guardar_ubicacion"), data, format="json")
    print(response.status_code, response.json())  # Depuración
    assert response.status_code == 201
"""