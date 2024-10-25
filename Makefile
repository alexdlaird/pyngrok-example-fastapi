.PHONY: all nopyc clean install test

SHELL := /usr/bin/env bash
PYTHON_BIN ?= python
PROJECT_VENV ?= venv

all: test

venv:
	$(PYTHON_BIN) -m pip install virtualenv --user
	$(PYTHON_BIN) -m virtualenv $(PROJECT_VENV)

install: venv
	@( \
		source $(PROJECT_VENV)/bin/activate; \
		python -m pip install -r requirements.txt -r requirements-dev.txt; \
	)

nopyc:
	find . -name '*.pyc' | xargs rm -f || true
	find . -name __pycache__ | xargs rm -rf || true

clean: nopyc
	rm -rf _build dist *.egg-info $(PROJECT_VENV)

test: install
	@( \
		source $(PROJECT_VENV)/bin/activate; \
		pytest -v; \
	)
