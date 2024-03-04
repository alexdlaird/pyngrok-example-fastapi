__copyright__ = "Copyright (c) 2023-2024 Alex Laird"
__license__ = "MIT"

import os

from fastapi.testclient import TestClient

os.environ["USE_NGROK"] = "False"
from pyngrokexamplefastapi.server import app

client = TestClient(app)


def test_healthcheck_no_ngrok():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"server": "up"}
