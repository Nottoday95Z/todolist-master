import json

from rest_framework.test import APIClient
import pytest
from django.urls import reverse

from core.models import User
from goals.models import GoalCategory, Goal
from goals.serializers import GoalSerializer


@pytest.mark.django_db
def test_create(auth_user: APIClient, add_user: User, category: GoalCategory) -> None:
    response = auth_user.post(
        reverse("goal_create"),
        data={
            "title": "test goal",
            "user": add_user.pk,
            "category": category.pk,
        },
    )
    expected_response = {
        "id": response.data.get("id"),
        "title": "test goal",
        "description": None,
        "due_date": None,
        "status": 1,
        "priority": 2,
        "category": category.pk,
        "created": response.data.get("created"),
        "updated": response.data.get("updated"),
    }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_retrieve(auth_user: APIClient, goal: Goal, add_user: User, category: GoalCategory) -> None:
    response = auth_user.get(reverse("goal_pk", args=[goal.pk]))

    expected_response = GoalSerializer(instance=goal).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_delete(auth_user: APIClient, goal: Goal, category: GoalCategory) -> None:
    response = auth_user.delete(reverse("goal_pk", args=[goal.pk]))

    assert response.status_code == 204


@pytest.mark.django_db
def test_update(auth_user: APIClient, goal: Goal, add_user: User, category: GoalCategory) -> None:
    response = auth_user.put(
        reverse("goal_pk", args=[goal.pk]),
        data=json.dumps({
            "title": "put goal",
            "category": category.pk
        }),
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.data.get("title") == "put goal"