from http import HTTPStatus

import pytest
import requests
from requests import Response

from shemas.user import User, Users


def test_users_no_duplicates(app_url: str):
    response: Response = requests.get(f"{app_url}/api/users/")
    users_ids = [user["id"] for user in response.json()['items']]
    assert len(users_ids) == len(set(users_ids))


@pytest.mark.parametrize("user_id", [1, 6, 12])
def test_user_id(app_url: str, user_id: int):
    response: Response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.OK
    User.model_validate(response.json())


@pytest.mark.parametrize("user_id", [13])
def test_user_nonexistent_values(app_url: str, user_id: int):
    response: Response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize("user_id", [-1, 0, "fafaf"])
def test_user_invalid_values(app_url: str, user_id: int):
    response: Response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_users(app_url: str):
    response: Response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    Users.model_validate(response.json())
