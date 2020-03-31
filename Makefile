SHELL := /bin/bash
.DEFAULT_GOAL := default
.PHONY: \
	help default run run-static \
	all all-no-cache \
	purge clean clean-all clean-stores clean-python \
	prune build build-static build-no-cache \
	up down down-all \
	python-dev-build tox

HELP_PADDING = 28
bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)
padded_str := %-$(HELP_PADDING)s
pretty_command := $(bold)$(padded_str)$(sgr0)

include .env  # environment variables used in docker-compose stack

MAKEFILE_DIR = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

PRUNE_OPTS = -f

BUILDKIT = 1
BUILD_OPTS = 
BUILD_NO_CACHE_OPT = --no-cache

DOWN_OPTS = --remove-orphans
DOWN_ALL_OPTS = ${DOWN_OPTS} --rmi all -v

UP_OPTS =

PYTHON_DEV_CMD = 

CHK_PORT = ${MLFLOW_TRACKING_SERVER_PORT}

help:
	@printf "======= General ======\n"
	@printf "$(pretty_command): run \"run\" (see below)\n" \(default\)
	@printf "$(pretty_command): run \"clean\", \"build\" and \"up\"\n" run
	@printf "$(pretty_command): run \"clean\", \"build-static\" and \"up\"\n" run
	@printf "$(pretty_command): run \"clean\", \"clean-stores\", \"build\" and \"up\"\n" all
	@printf "$(pretty_command): run \"clean-all\", \"build-no-cache\" and \"up\"\n" all-no-cache
	@printf "\n"
	@printf "======= Cleanup ======\n"
	@printf "$(pretty_command): run \"down\" and \"prune\"\n" clean
	@printf "$(pretty_command): run \"down-all\", \"prune\" and \"clean-stores\"\n" clean-all
	@printf "$(pretty_command): remove local folders mounted as volumes in docker-compose\n" clean-stores
	@printf "$(pretty_command): clean python-related artifacts\n" clean-python
	@printf "$(pretty_command): alias of \"clean-all\"\n" purge
	@printf "\n"
	@printf "======= Docker =======\n"
	@printf "$(pretty_command): Remove all unused docker containers, networks and images \n" prune
	@printf "$(padded_str)PRUNE_OPTS, \"docker system prune\" options (default: $(PRUNE_OPTS))\n"
	@printf "$(pretty_command): build the docker-compose stack; python code is installed to the Jupyter service as editable\n" build
	@printf "$(padded_str)BUILD_OPTS, \"docker-compose build\" options (default: $(BUILD_OPTS))\n"
	@printf "$(pretty_command): build the docker-compose stack; python code is install to the Jupyter service as static\n" build-static
	@printf "$(pretty_command): build docker-compose stack with \"${BUILD_NO_CACHE_OPT}\"\n" build-no-cache
	@printf "$(pretty_command): start the docker-compose stack\n" up
	@printf "$(padded_str)UP_OPTS, \"docker-compose up\" options (default: $(UP_OPTS))\n"
	@printf "$(pretty_command): stop the docker-compose stack and remove artifacts created by \"up\"\n" down
	@printf "$(padded_str)DOWN_OPTS, \"docker-compose down\" options (default: $(DOWN_OPTS))\n"
	@printf "$(pretty_command): build docker-compose stack with \"${DOWN_ALL_OPTS}\"\n" down-all
	@printf "$(pretty_command): build \"python-dev\" image\n" python-dev-build
	@printf "$(pretty_command): run automated checks inside \"python-dev\" using tox\n" tox
	@printf "\n"
	@printf "========= Misc =======\n"
	@printf "$(pretty_command): identify applications, which are bound to the given port. Useful for freeing ports from phantom tasks\n" find_port_usage
	@printf "$(padded_str)CHK_PORT, Port to check (default: $(CHK_PORT))\n"

default: run

run: clean build up
run-static: clean build-static up
all: clean clean-stores build up
all-no-cache: clean-all build-no-cache up

purge: clean-all
clean-all: down-all prune clean-stores clean-python
clean: down prune
clean-stores:
	sudo rm -rf .${MLFLOW_ARTIFACT_STORE} ${POSTGRES_STORE}

clean-python:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	rm -rf .pytest_cache
	find . -name '.eggs' -type d -exec rm -rf {} +
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

prune:
	docker system prune ${PRUNE_OPTS}

build: 
	DOCKER_BUILDKIT=${BUILDKIT} JUPYTER_TARGET=${JUPYTER_TARGET} docker-compose build ${BUILD_OPTS}
build-static: JUPYTER_TARGET := ${JUPYTER_STATIC_TARGET}
build-static: build

build-no-cache: BUILD_OPTS:=$(BUILD_NO_CACHE_OPT)
build-no-cache: build

up: 
	mkdir -p ${MLFLOW_ARTIFACT_STORE} ${POSTGRES_STORE};
	docker-compose up ${UP_OPTS}

down:
	docker-compose down ${DOWN_OPTS}
down-all: DOWN_OPTS := ${DOWN_ALL_OPTS}
down-all: down

python-dev-build:	
	DOCKER_BUILDKIT=${BUILDKIT} docker build . -f ./docker/python-dev/Dockerfile -t sertansenturk/python-dev:${VERSION} ${BUILD_OPTS}

tox: PYTHON_DEV_CMD := tox
tox: python-dev-build
	docker run -it sertansenturk/python-dev:${VERSION} ${PYTHON_DEV_CMD}

find_port_usage:
	sudo lsof -i -P -n | grep ${CHK_PORT}
