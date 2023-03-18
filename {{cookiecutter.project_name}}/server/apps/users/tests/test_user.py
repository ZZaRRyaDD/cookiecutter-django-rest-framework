import pytest

from django.urls import reverse_lazy
from rest_framework import status

from apps.users.factories import UserFactory


pytestmark = pytest.mark.django_db


def test_retrieve_user(api_client) -> None:
    UserFactory.create()
    api_client.force_authenticate()
    response = api_client.get(
        reverse_lazy("api:users-detail"),
    )
    assert response.status_code == status.HTTP_200_OK
