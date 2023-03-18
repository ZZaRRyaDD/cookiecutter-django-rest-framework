import pytest
from django.urls import reverse_lazy
from rest_framework import status

from apps.users.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_retrieve_user(api_client) -> None:
    user = UserFactory.create()
    api_client.force_authenticate(user=user)
    response = api_client.get(
        reverse_lazy(
            "api:users-detail",
            kwargs={"pk": user.pk},
        ),
    )
    assert response.status_code == status.HTTP_200_OK


def test_retrieve_user_me(api_client) -> None:
    user = UserFactory.create()
    api_client.force_authenticate(user=user)
    response = api_client.get(
        reverse_lazy(
            "api:users-me",
        ),
    )
    assert response.status_code == status.HTTP_200_OK
