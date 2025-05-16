__copyright__ = "Copyright (c) 2023-2024 Alex Laird"
__license__ = "MIT"

import os
import unittest

from fastapi.testclient import TestClient
from pyngrok import process, conf

from pyngrokexamplefastapi.server import create_app

os.environ["USE_NGROK"] = "True"

app = create_app()
client = TestClient(app)


@unittest.skipIf(not os.environ.get("NGROK_AUTHTOKEN"), "NGROK_AUTHTOKEN environment variable not set")
def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"server": "up"}
    assert "ngrok" in app.settings.BASE_URL
    assert process.is_process_running(conf.get_default().ngrok_path)
