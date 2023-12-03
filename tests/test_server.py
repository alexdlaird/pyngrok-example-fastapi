from fastapi.testclient import TestClient

from pyngrokexamplefastapi.server import app

client = TestClient(app)


def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"server": "up"}
