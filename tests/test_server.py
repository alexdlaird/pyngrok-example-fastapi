import os
import unittest

from fastapi.testclient import TestClient

os.environ["USE_NGROK"] = "True"
from pyngrokexamplefastapi.server import app

client = TestClient(app)


@unittest.skipIf(not os.environ.get("NGROK_AUTHTOKEN"), "NGROK_AUTHTOKEN environment variable not set")
def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"server": "up"}
