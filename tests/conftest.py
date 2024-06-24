import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from fast_api_zero.app import app
from fast_api_zero.models import table_registry


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(bind=engine)
