import os
import unittest

from fastapi.testclient import TestClient

os.environ["USE_NGROK"] = "True"
from pyngrokexamplefastapi.server import app

client = TestClient(app)


@unittest.skipIf("NGROK_AUTHTOKEN" not in os.environ, "NGROK_AUTHTOKEN environment variable not set")
def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"server": "up"}
