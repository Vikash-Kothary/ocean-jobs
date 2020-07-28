#!/usr/bin/make

SHELL := "$(shell which bash)"
OCEAN_JOBS_NAME ?= "OCEAN Jobs"
OCEAN_JOBS_VERSION ?= "v0.1.0"
OCEAN_JOBS_DESCRIPTION ?= "There's plenty of jobs in the ocean."
ENV ?= local

include config/.env.${ENV}
export

.DEFAULT_GOAL := help
.PHONY: help #: Display a list of command and exit.
help:
	@awk 'BEGIN {FS = " ?#?: "; print ""$(OCEAN_JOBS_NAME)" "$(OCEAN_JOBS_VERSION)"\n"$(OCEAN_JOBS_DESCRIPTION)"\n\nUsage: make \033[36m<command>\033[0m\n\nCommands:"} /^.PHONY: ?[a-zA-Z_-]/ { printf "  \033[36m%-10s\033[0m %s\n", $$2, $$3 }' $(MAKEFILE_LIST)

.PHONY: docs
docs: print-env
	@$(MKDOCS) serve -f docs/mkdocs.yml

.PHONY: lint
lint: print-env
	@$(FLAKE8) src tests

.PHONY: notebooks #: Develop using Jupyter Lab.
notebooks: print-env
	@$(JUPYTER) lab

.PHONY: tests
tests: print-env
	@$(PYTEST) tests

.PHONY: run
run: print-env
	@$(FLASK) run

clean: print-env
	@[[ -z "${FORCE}" ]] || rm -r .venv
	@find . -name __pycache__ -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name *.pytest_cache -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name *.egg-info -type d -not -path .venv -print0 | xargs -0 rm -r

%:
	@sh scripts/$(*).sh
