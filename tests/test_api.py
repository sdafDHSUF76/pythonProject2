import json
from http import HTTPStatus

import pytest
import requests
from _pytest.python import Metafunc

from models.user import User, Users
from models.error_list import ErrorParams


def test_users_no_duplicates(app_url):
    response = requests.get(f"{app_url}/api/users/")
    users_ids = [user["id"] for user in response.json()['items']]
    assert len(users_ids) == len(set(users_ids))


@pytest.mark.parametrize("user_id", [1, 6, 12])
def test_user_id(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.OK
    User.model_validate(response.json())


@pytest.mark.parametrize("user_id", [13])
def test_user_nonexistent_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize("user_id", [-1, 0, "fafaf"])
def test_user_invalid_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


page_and_size = [(-1, -1), (999999, 999999), (0,0), ("fafaf", "fafaf")]


def pytest_generate_tests(metafunc: Metafunc):
    with open("C:\\Users\\Y\\pythonProject2\\users.json") as f:
        users = json.load(f)
    if 'page_and_size_parametrize' in metafunc.fixturenames:
        # Generate test cases based on the user_roles list

        new_data_page_and_size = [
            (len(users) + 1, len(users)),
            (len(users), len(users) + 1),
            (len(users) + 1, len(users) + 1),
            (1, 1)
        ]
        metafunc.parametrize('page_and_size_parametrize', new_data_page_and_size)


    if 'data_page' in metafunc.fixturenames:
        new_data_page = [
            len(users),
            1,
            99999999,
            *(lambda:[2] if len(users) > 1 else [])()
        ]
        metafunc.parametrize('data_page', new_data_page)

    if 'data_size' in metafunc.fixturenames:
        new_data_size = [
            len(users),
            1,
            *(lambda:[2] if len(users) > 1 else [])()
        ]
        metafunc.parametrize('data_size', new_data_size)


@pytest.mark.parametrize("page, size", [
    (-1, -1),
    (999999, 999999),
    (0, 0),
    ("fafaf", "fafaf"),
    ("@/*$%^&#*/()?>,.*/\"", "@/*$%^&#*/()?>,.*/\""),
    ('None', 'None'),
])
def test_users_invalid_page_and_size(app_url: str, page: int, size: int):
    response = requests.get(f"{app_url}/api/users/?page={page}&size={size}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    a = response.json()
    ErrorParams.parse_obj(response.json())


def test_users_boundary_values_page_and_size(app_url: str, page_and_size_parametrize: tuple[int, int]):
    page, size = page_and_size_parametrize
    response = requests.get(f"{app_url}/api/users/?page={page}&size={size}")
    assert response.status_code == HTTPStatus.OK
    Users.parse_obj(response.json())


@pytest.mark.parametrize("page", [-1, 0, "fafaf", "@/*$%^&#*/()?>,.*/\"", 'None'])
def test_users_invalid_page(app_url: str, page: int | str):
    response = requests.get(f"{app_url}/api/users/?page={page}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    ErrorParams.parse_obj(response.json())

@pytest.mark.parametrize("size", [-1, 0, "fafaf", "@/*$%^&#*/()?>,.*/\"", 99999999, 'None'])
def test_users_invalid_size(app_url: str, size: int | str):
    response = requests.get(f"{app_url}/api/users/?size={size}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    ErrorParams.parse_obj(response.json())


# @pytest.mark.parametrize("page", [1, 12])
def test_users_page(app_url: str, data_page: int):
    response = requests.get(f"{app_url}/api/users/?page={data_page}")
    assert response.status_code == HTTPStatus.OK
    Users.parse_obj(response.json())

# @pytest.mark.parametrize("size", [-1, 0, "fafaf", "@/*$%^&#*/()?>,.*/\"", 99999999, 'None'])
def test_users_size(app_url: str, data_size: int):
    response = requests.get(f"{app_url}/api/users/?size={data_size}")
    assert response.status_code == HTTPStatus.OK
    Users.parse_obj(response.json())


def test_users(app_url: str):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    Users.parse_obj(response.json())
