import json

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import User
from goals.models import Board, GoalCategory
from goals.serializers import GoalCategorySerializer


@pytest.mark.django_db
def test_retrieve(auth_user: APIClient, add_user: User, category: GoalCategory, board: Board) -> None:
    response = auth_user.get(reverse("goal_category_pk", args=[category.pk]))

    expected_response = GoalCategorySerializer(instance=category).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_update(auth_user: APIClient, board: Board, add_user: User, category: GoalCategory) -> None:
    response = auth_user.put(
        reverse("goal_category_pk", args=[category.pk]),
        data=json.dumps({
            "title": "put category",
            "board": board.pk
        }),
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.data.get("title") == "put category"