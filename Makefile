#!/usr/bin/make

SHELL := "$(shell which bash)"
OCEAN_JOBS_NAME ?= "OCEAN Jobs"
OCEAN_JOBS_VERSION ?= "v0.1.0"
OCEAN_JOBS_DESCRIPTION ?= "There's plenty of jobs in the ocean."

-include .env
export

.DEFAULT_GOAL := help
.PHONY: help #: Display a list of command and exit.
help:
	@awk 'BEGIN {FS = " ?#?: "; print ""$(OCEAN_JOBS_NAME)" "$(OCEAN_JOBS_VERSION)"\n"$(OCEAN_JOBS_DESCRIPTION)"\n\nUsage: make \033[36m<command>\033[0m\n\nCommands:"} /^.PHONY: ?[a-zA-Z_-]/ { printf "  \033[36m%-10s\033[0m %s\n", $$2, $$3 }' $(MAKEFILE_LIST)

.PHONY: init #: Download dependencies.
init:
	@poetry install

.PHONY: lint
lint:
	@flake8 src tests

.PHONY: notebooks #: Develop using Jupyter Lab.
notebooks:
	@jupyter lab

.PHONY: tests
tests:
	@pytest tests

.PHONY: run
run:
	@flask run

clean:
	@[[ -z "${FORCE}" ]] || rm -r .venv
	@find . -name *.pytest_cache -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name *.egg-info -type d -not -path .venv -print0 | xargs -0 rm -r

%:
	@sh scripts/$(*).sh
