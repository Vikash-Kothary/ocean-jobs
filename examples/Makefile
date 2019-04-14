#!make
# Makefile for Ocean Jobs Examples

-include .env
export

# Commands:
.PHONY: init build install run tests examples clean-pyc clean-build
SHELL := /bin/bash
EXAMPLES_CONTEXT := $(or $(EXAMPLES_CONTEXT),.)

#@ - examples: Run jupyter notebook.
examples:
	@source .venv/bin/activate && \
	cd ${EXAMPLES_CONTEXT}/ && \
	jupyter notebook --notebook-dir=../examples/