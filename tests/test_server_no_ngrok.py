__copyright__ = "Copyright (c) 2023-2024 Alex Laird"
__license__ = "MIT"

import os

from fastapi.testclient import TestClient

from pyngrokexamplefastapi.server import create_app

os.environ["USE_NGROK"] = "False"

app = create_app()
client = TestClient(app)


def test_healthcheck_no_ngrok():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"server": "up"}
    assert "ngrok" not in app.settings.BASE_URL
