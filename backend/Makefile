#!make
# Makefile for Ocean Jobs Backend

-include .env
export

# Commands:
.PHONY: init build install run tests examples clean-pyc clean-build
SHELL := /bin/bash
BACKEND_CONTEXT := $(or $(BACKEND_CONTEXT),.)
PROJECT_NAME := $(shell python setup.py --name)}

#@ - init: Install requirements.
init:
	@python3 -m venv .venv && \
	.venv/bin/pip3 install -r ${BACKEND_CONTEXT}/requirements.txt

#@ - run: Run backend.
run:
	@source .venv/bin/activate && \
	@cd ${BACKEND_CONTEXT}/ && \
	python3 main.py

#@ - tests: Run tests.
tests:
	@source .venv/bin/activate && \
	cd ${BACKEND_CONTEXT}/ && \
	python3 -m pytest --doctest-modules

#@ - build: Build python package.
build:
	source .venv/bin/activate && \
	cd ${BACKEND_CONTEXT}/ && \
	python3 setup.py build

#@ - install: Install python package.
install: build
	@source .venv/bin/activate && \
	cd ${BACKEND_CONTEXT}/ && \
	python3 setup.py install

#@ - clean: Remove python genenerated files
clean: clean-pyc clean-build

clean-pyc:
	@find . -type d -name '__pycache__' -exec rm --force --recursive {} +
	@find . -name '*.pyc' -exec rm --force {} +
	@find . -name '*.pyo' -exec rm --force {} +
	#@name '*~' -exec rm --force  {} 

clean-build:
	@rm --force --recursive build/
	@rm --force --recursive dist/
	@rm --force --recursive *.egg-info
