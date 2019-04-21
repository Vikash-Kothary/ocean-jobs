#!make
#@ Makefile for Ocean Jobs

#@ Commands:
.PHONY: help

BACKEND_CONTEXT := backend
-include ${BACKEND_CONTEXT}/Makefile
EXAMPLES_CONTEXT := examples
-include ${EXAMPLES_CONTEXT}/Makefile

#@ - help: Show all commands.
help:
	@fgrep -h "#@" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/#@ //'
