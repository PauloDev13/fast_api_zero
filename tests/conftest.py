import pytest
from starlette.testclient import TestClient

from fast_api_zero.app import app


@pytest.fixture()
def client():
    return TestClient(app)
