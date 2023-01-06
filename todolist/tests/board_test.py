import json

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import User
from goals.models import Board, BoardParticipant
from goals.serializers import BoardSerializer, BoardListSerializer
from tests.factories import BoardFactory, BoardParticipantFactory


@pytest.mark.django_db
def test_create(auth_user: APIClient, board: Board) -> None:
    response = auth_user.post(
        reverse('create_board'),
        data={
            'title': 'test board',
        },
    )
    expected_response = {
        'id': response.data.get('id'),
        'title': 'test board',
        'created': response.data.get('created'),
        'updated': response.data.get('updated'),
        'is_deleted': False,
    }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_list(auth_user: APIClient, board: Board, add_user: User) -> None:
    board_ = BoardFactory.create(title='test board')
    participant = BoardParticipantFactory.create(board=board_, user=add_user)
    response = auth_user.get(f"{reverse('list_board')}?limit=1")
    expected_response = {
        'count': 1,
        'next': None,
        'previous': None,
        'results': BoardListSerializer(instance=(board_,), many=True).data
    }

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_retrieve(auth_user: APIClient, board: Board, add_user: User, board_participant: BoardParticipant) -> None:
    response = auth_user.get(reverse('retrieve_board', args=[board.pk]))

    expected_response = BoardSerializer(instance=board).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_delete(auth_user: APIClient, board: Board, add_user: User, board_participant: BoardParticipant) -> None:
    response = auth_user.delete(reverse('retrieve_board', args=[board.pk]))

    assert response.status_code == 204


@pytest.mark.django_db
def test_update(auth_user: APIClient, board: Board, add_user: User, board_participant: BoardParticipant) -> None:
    response = auth_user.put(
        reverse('retrieve_board', args=[board.pk]),
        data=json.dumps({
            'title': 'put board',
            'participants': [],
        }),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.data.get('title') == 'put board'