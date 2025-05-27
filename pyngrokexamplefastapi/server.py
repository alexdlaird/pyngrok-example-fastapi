__copyright__ = "Copyright (c) 2023-2024 Alex Laird"
__license__ = "MIT"

import os
import sys

from fastapi import FastAPI
from fastapi.logger import logger
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ... Implement the rest of your FastAPI settings

    BASE_URL: str = "http://localhost:8000"
    USE_NGROK: bool = os.environ.get("USE_NGROK", "False") == "True"


def init_webhooks(base_url):
    # ... Implement updates necessary so inbound traffic uses the public-facing ngrok URL
    pass


def create_app():
    # Initialize the FastAPI app for a simple web server
    app = FastAPI()
    app.settings = Settings()

    if app.settings.USE_NGROK:
        # Only import pyngrok and install if we're actually going to use it
        from pyngrok import ngrok

        # Get the dev server port (defaults to 8000 for Uvicorn, can be overridden with `--port`
        # when starting the server
        port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else "8000"

        # Open a ngrok tunnel to the dev server
        public_url = ngrok.connect(port).public_url
        logger.info(f"ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

        # Update any base URLs or webhooks to use the public ngrok URL
        app.settings.BASE_URL = public_url
        init_webhooks(public_url)

    # ... Implement routers and the rest of your app
    @app.get('/healthcheck')
    def get_healthcheck():
        return {"server": "up"}

    return app
