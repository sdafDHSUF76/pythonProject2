import os

import dotenv
import pytest
from typing import TYPE_CHECKING

from test_smoke import test_server_is_ready

from _pytest.nodes import Node

if TYPE_CHECKING:
    from _pytest.main import Session


@pytest.fixture(scope='session', autouse=True)
def envs():
    dotenv.load_dotenv('C:\\Users\\Y\\pythonProject2\\.env.sample')


@pytest.fixture
def app_url() -> str:
    return os.getenv("APP_URL")


@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(config, items):
    for item in items:
        if item.originalname == 'test_server_is_ready':
            return
    new_test: Node = pytest.Function.from_parent(
        parent=items[0].parent,  # Указываем родительский объект
        name=test_server_is_ready.__name__,  # Имя теста
        callobj=test_server_is_ready  # Функция теста
    )
    items.append(new_test)


@pytest.hookimpl(wrapper=True)
def pytest_runtestloop(session: 'Session'):
    if session.items[0].originalname == 'test_server_is_ready':
        pass
    else:
        session.ihook.pytest_runtest_protocol(item=session.items[-1], nextitem=None)
        if session.testsfailed:
            session.shouldstop = True
        session.items.remove(session.items[-1])
        pass
    outcome = yield