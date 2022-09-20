import pytest
from main import create_app
from fastapi.testclient import TestClient


@pytest.fixture()
def app():
    app, _, _ = create_app()
    return app


@pytest.fixture()
def client(app):
    return TestClient(app)


def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Python Para Finanças - test"}
