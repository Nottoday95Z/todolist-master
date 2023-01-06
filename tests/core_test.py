import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import User
from core.serializers import ProfileSerializer


@pytest.mark.django_db
def test_login(client: APIClient, add_user: User) -> None:
    response = client.post(
        reverse("login"),
        data={
            "username": "newtestuser",
            "password": "super1Password",
        },
        content_type="application/json",
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_profile(auth_user: APIClient, add_user: User) -> None:
    response = auth_user.get(reverse("profile"))
    expected_response = ProfileSerializer(instance=add_user).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_update_password(auth_user: APIClient, add_user: User) -> None:
    response = auth_user.put(
        reverse("update_password"),
        data={
            "new_password": "super3Password",
            "old_password": "super1Password",
        },
    )

    assert response.status_code == 200