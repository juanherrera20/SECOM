from django.urls import reverse

from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
def test_evento_list_view():
    client = APIClient()
    response = client.get(reverse("evento-list"))
    assert response.status_code == 200
