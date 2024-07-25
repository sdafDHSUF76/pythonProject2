from http import HTTPStatus

import pytest
import requests
from requests import Response


@pytest.mark.smoke
def test_server_is_ready(app_url: str):
    response: Response = requests.get(f"{app_url}/status")
    assert response.status_code == HTTPStatus.OK
