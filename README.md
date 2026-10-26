[![Build](https://img.shields.io/github/actions/workflow/status/alexdlaird/pyngrok-example-fastapi/build.yml)](https://github.com/alexdlaird/pyngrok-example-fastapi/actions/workflows/build.yml)
![GitHub License](https://img.shields.io/github/license/alexdlaird/pyngrok-example-fastapi)

# pyngrok Example - FastAPI

This is an example project that shows how to easily integrate [`pyngrok`](https://github.com/alexdlaird/pyngrok)
with [FastAPI](https://fastapi.tiangolo.com/), as [summarized in the docs](https://pyngrok.readthedocs.io/en/latest/integrations.html#fastapi).

## Running

To run the example locally, install its dependencies, then start the server with `USE_NGROK` set to open a tunnel.
The tunnel's public URL is printed when the server starts.

```sh
make install
USE_NGROK=True NGROK_AUTHTOKEN=$NGROK_AUTHTOKEN venv/bin/uvicorn pyngrokexamplefastapi.server:create_app --factory
```

To run the tests, use `make test`. Tests that open a tunnel are skipped if `NGROK_AUTHTOKEN` isn't set.