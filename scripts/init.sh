#!/bin/bash
# file: init.sh
# description: Download dependencies based on environment.

if [[ "${ENV}" == "ci" ]]; then
	pip install toml # Need to be preinstalled to use package setup.py.
	pip install -r src/requirements-dev.txt
elif [[ "${ENV}" == "local" ]]; then
	make lock
	poetry install
	poetry run pre-commit install
elif [[ "${ENV}" == "dev" ]]; then
	docker-compose up
fi