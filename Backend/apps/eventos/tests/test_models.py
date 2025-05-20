import pytest
from apps.eventos.models import Evento, Donation, Subscription
from apps.usuarios.models import CustomUser
from apps.ubicacion.models import Ubicacion, City, Departamento
from datetime import date

@pytest.mark.django_db
def test_evento_str():
    user = CustomUser.objects.create_user(username="testuser", email="test@example.com", password="pass1234")
    depto = Departamento.objects.create(name="Meta")
    city = City.objects.create(name="Villavicencio", departamento=depto, latitude=4.15, longitude=-73.63)
    ubicacion = Ubicacion.objects.create(name="Parque", city=city, address="Carrera 30", pais="Colombia")
    donation = Donation.objects.create(name="Ropa")
    evento = Evento.objects.create(
        name="Evento Test", description="Descripción", meet_date=date.today(),
        ubicacion=ubicacion, organizador=user, type_donation=donation
    )
    assert "Evento Test" in str(evento)
