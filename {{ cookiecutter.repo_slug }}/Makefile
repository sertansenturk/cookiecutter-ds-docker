SHELL := /bin/bash
.DEFAULT_GOAL := default
.PHONY: \
	help default lab notebook \
	scipy tensorflow pyspark \
	test chk-store-permissions all \
	purge clean clean-all clean-stores clean-python \
	prune build \
	up run down down-all \
	python-dev-build tox \
	sphinx-build sphinx-clean sphinx-apidoc sphinx-html sphinx-html-test \
	find-port-usage debug-travis

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

DOWN_OPTS = --remove-orphans
DOWN_ALL_OPTS = ${DOWN_OPTS} --rmi all -v

UP_OPTS =
RUN_OPTS =

PYTHON_DEV_CMD =

DOCS_FOLDER = docs
SPHINX_OPTS := -nWT -b linkcheck --keep-going

CHK_PORT = ${MLFLOW_TRACKING_SERVER_PORT}

HOST_USERNAME := $(shell id -u -n)

JUPYTER_BASE_IMAGE := ${JUPYTER_SCIPY_IMAGE}
JUPYTER_BASE_VERSION := ${JUPYTER_SCIPY_VERSION}

JUPYTER_CHOWN_EXTRA := "/${DATA_DIR}"
JUPYTER_UID := $(shell id -u)
JUPYTER_USERNAME := $(shell id -u -n)

POSTGRES_UID := $(shell id -u)
POSTGRES_GID := $(shell id -g)

TRAVIS_JOB =
TRAVIS_TOKEN =

help:
	@printf "======= General ======\n"
	@printf "$(pretty_command): alias of \"make lab\" (see below)\n" \(default\)
	@printf "$(pretty_command): start docker stack with JupyterLab from ${JUPYTER_BASE_IMAGE} with the python repo installed as editable\n" lab
	@printf "$(pretty_command): start docker stack with JupyterLab from ${JUPYTER_SCIPY_IMAGE}\n" scipy
	@printf "$(pretty_command): start docker stack with JupyterLab from ${JUPYTER_TENSORFLOW_IMAGE}\n" tensorflow
	@printf "$(pretty_command): start docker stack with JupyterLab from ${JUPYTER_PYSPARK_IMAGE}\n" pyspark
	@printf "$(pretty_command): start docker stack with classic Jupyter notebook interface\n" notebook
	@printf "$(pretty_command): run docker stack with tests\n" test
	@printf "$(pretty_command): run \"clean\", \"clean-stores\", \"build\" and \"up\"\n" all
	@printf "\n"
	@printf "======= Cleanup ======\n"
	@printf "$(pretty_command): run \"down\" and \"prune\"\n" clean
	@printf "$(pretty_command): run \"down-all\", \"prune\", \"clean-python\" and \"clean-stores\"\n" clean-all
	@printf "$(pretty_command): remove local folders mounted as volumes in docker-compose\n" clean-stores
	@printf "$(pretty_command): clean python-related artifacts\n" clean-python
	@printf "$(pretty_command): alias of \"clean-all\"\n" purge
	@printf "\n"
	@printf "======= Docker =======\n"
	@printf "$(pretty_command): Remove all unused docker containers, networks and images \n" prune
	@printf "$(padded_str)PRUNE_OPTS, \"docker system prune\" options (default: $(PRUNE_OPTS))\n"
	@printf "$(pretty_command): build the docker-compose stack with the python code is installed on the Jupyter service as editable\n" build
	@printf "$(padded_str)BUILD_OPTS, \"docker-compose build\" options (default: $(BUILD_OPTS))\n"
	@printf "$(pretty_command): docker-compose up\n" up
	@printf "$(padded_str)UP_OPTS, \"docker-compose up\" options (default: $(UP_OPTS))\n"
	@printf "$(pretty_command): docker-compose run\n" run
	@printf "$(padded_str)RUN_OPTS, \"docker-compose run\" options (default: $(RUN_OPTS))\n"
	@printf "$(pretty_command): docker-compose down and remove the created artifacts\n" down
	@printf "$(padded_str)DOWN_OPTS, \"docker-compose down\" options (default: $(DOWN_OPTS))\n"
	@printf "$(pretty_command): docker-compose down with \"${DOWN_ALL_OPTS}\"\n" down-all
	@printf "$(pretty_command): build \"python-dev\" image\n" python-dev-build
	@printf "$(pretty_command): run automated checks inside \"python-dev\" using tox\n" tox
	@printf "\n"
	@printf "======= Documentation ======\n"
	@printf "$(pretty_command): builds sphinx docker image\n" sphinx-build
	@printf "$(pretty_command): cleans documentation at \"./docs/_build/\"\n" sphinx-clean
	@printf "$(pretty_command): creates rst documentation from python docstring\n" sphinx-apidoc
	@printf "$(pretty_command): builds sphinx html docs at \"./docs/_build/html\"\n" sphinx-html
	@printf "$(padded_str)SPHINX_OPTS, options to pass to sphinx (default: $(SPHINX_OPTS))\n"
	@printf "$(pretty_command): tests sphinx html build\n" sphinx-html-test
	@printf "\n"
	@printf "========= Misc =======\n"
	@printf "$(pretty_command): create the local mlflow artifact store\n" ${MLFLOW_ARTIFACT_STORE}
	@printf "$(pretty_command): create the local posgres store\n" ${POSTGRES_STORE}
	@printf "$(pretty_command): identify applications, which are bound to the given port. Useful for freeing ports from phantom tasks\n" find-port-usage
	@printf "$(padded_str)CHK_PORT, Port to check (default: $(CHK_PORT))\n"
	@printf "$(pretty_command): send a job debug request to travis\n" debug-travis
	@printf "$(padded_str)TRAVIS_TOKEN, travis api token (default: $(TRAVIS_TOKEN))\n"
	@printf "$(padded_str)TRAVIS_JOB, travis job id (default: $(TRAVIS_JOB))\n"

default: clean build up
lab: default

notebook: JUPYTER_ENABLE_LAB:=
notebook: default

scipy: JUPYTER_BASE_IMAGE=${JUPYTER_SCIPY_IMAGE}
scipy: JUPYTER_BASE_VERSION=${JUPYTER_SCIPY_VERSION}
scipy: default

tensorflow: JUPYTER_BASE_IMAGE=${JUPYTER_TENSORFLOW_IMAGE}
tensorflow: JUPYTER_BASE_VERSION=${JUPYTER_TENSORFLOW_VERSION}
tensorflow: default

pyspark: JUPYTER_BASE_IMAGE=${JUPYTER_PYSPARK_IMAGE}
pyspark: JUPYTER_BASE_VERSION=${JUPYTER_PYSPARK_VERSION}
pyspark: default

test: JUPYTER_TARGET:=${JUPYTER_TEST_TARGET}
test: RUN_OPTS:=jupyter start.sh ./run_pytest.sh ${MLFLOW_IMAGE_NAME} ${MLFLOW_TRACKING_SERVER_PORT} ${WAIT_FOR_IT_TIMEOUT}
test: JUPYTER_CHOWN_EXTRA:="/${DATA_DIR},/tests"
test: clean build run chk-store-permissions
	$(MAKE) down
# NOTE: above, `clean` had already called `down` so we had to make
# an explicit recursive call by `$(MAKE) down` 

chk-store-permissions:
	@if [ $(shell find data ! -user ${HOST_USERNAME} | wc -l) -gt 0 ]; then \
		echo "Found files and/or folders with wrong permission: " ; \
		echo "=> $(shell find data ! -user ${HOST_USERNAME} -printf '%p (%u) ')" ; \
		exit 1 ; \
	else \
		exit 0 ; \
	fi

all: clean clean-stores build up

purge: clean-all
clean-all: down-all prune clean-stores clean-python
clean: down prune
clean-stores:
	rm -rf ./${MLFLOW_ARTIFACT_STORE} ./${POSTGRES_STORE}

clean-python:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.ipynb_checkpoints' -exec rm -fr {} +
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
	DOCKER_BUILDKIT=${BUILDKIT} COMPOSE_DOCKER_CLI_BUILD=${BUILDKIT} \
	JUPYTER_BASE_IMAGE=${JUPYTER_BASE_IMAGE} JUPYTER_BASE_VERSION=${JUPYTER_BASE_VERSION} \
	JUPYTER_TARGET=${JUPYTER_TARGET} JUPYTER_USERNAME=${JUPYTER_USERNAME} \
	MLFLOW_VERSION=${MLFLOW_VERSION} \
	POSTGRES_UID=${POSTGRES_UID} POSTGRES_GID=${POSTGRES_GID} \
	docker-compose build ${BUILD_OPTS}

${MLFLOW_ARTIFACT_STORE}:
	mkdir -p ${MLFLOW_ARTIFACT_STORE}

${POSTGRES_STORE}:
	mkdir -p ${POSTGRES_STORE}

up: ${MLFLOW_ARTIFACT_STORE} ${POSTGRES_STORE}
	JUPYTER_BASE_IMAGE=${JUPYTER_BASE_IMAGE} JUPYTER_BASE_VERSION=${JUPYTER_BASE_VERSION} \
	JUPYTER_TARGET=${JUPYTER_TARGET} \
	JUPYTER_CHOWN_EXTRA=${JUPYTER_CHOWN_EXTRA} \
	JUPYTER_UID=${JUPYTER_UID} JUPYTER_USERNAME=${JUPYTER_USERNAME} \
	JUPYTER_ENABLE_LAB=${JUPYTER_ENABLE_LAB} \
	POSTGRES_UID=${POSTGRES_UID} POSTGRES_GID=${POSTGRES_GID} \
	docker-compose up ${UP_OPTS}

run: ${MLFLOW_ARTIFACT_STORE} ${POSTGRES_STORE}
	JUPYTER_BASE_IMAGE=${JUPYTER_BASE_IMAGE} JUPYTER_BASE_VERSION=${JUPYTER_BASE_VERSION} \
	JUPYTER_TARGET=${JUPYTER_TARGET} \
	JUPYTER_CHOWN_EXTRA=${JUPYTER_CHOWN_EXTRA} \
	JUPYTER_UID=${JUPYTER_UID} JUPYTER_USERNAME=${JUPYTER_USERNAME} \
	JUPYTER_ENABLE_LAB=${JUPYTER_ENABLE_LAB} \
	POSTGRES_UID=${POSTGRES_UID} POSTGRES_GID=${POSTGRES_GID} \
	docker-compose run ${RUN_OPTS}

down:
	docker-compose down ${DOWN_OPTS}
down-all: DOWN_OPTS:=${DOWN_ALL_OPTS}
down-all: down

python-dev-build:	
	DOCKER_BUILDKIT=${BUILDKIT} \
	docker build . \
		-f ./docker/python-dev/Dockerfile \
		-t ${IMAGE_OWNER}/${PYTHON_DEV_IMAGE_NAME}:${VERSION} \
		${BUILD_OPTS}

tox: PYTHON_DEV_CMD := tox
tox: python-dev-build
	docker run -it ${IMAGE_OWNER}/${PYTHON_DEV_IMAGE_NAME}:${VERSION} ${PYTHON_DEV_CMD}

sphinx-build:
	DOCKER_BUILDKIT=${BUILDKIT} \
	docker build \
		--build-arg SPHINX_VERSION=${SPHINX_VERSION} \
		. \
		-f ./docker/sphinx/Dockerfile \
		-t ${IMAGE_OWNER}/${SPHINX_IMAGE_NAME}:${SPHINX_VERSION}

sphinx-clean: sphinx-build
	docker run -it --rm \
		-v ${MAKEFILE_DIR}:/makam_recognition_experiments/ \
		${IMAGE_OWNER}/${SPHINX_IMAGE_NAME}:${SPHINX_VERSION} \
		make clean

sphinx-apidoc: sphinx-build
	docker run -it --rm \
		-v ${MAKEFILE_DIR}:/makam_recognition_experiments/ \
		${IMAGE_OWNER}/${SPHINX_IMAGE_NAME}:${SPHINX_VERSION} \
		sphinx-apidoc -f -o ./ ../src/mre

sphinx-html: sphinx-clean sphinx-apidoc
	docker run -it --rm \
		-v ${MAKEFILE_DIR}:/makam_recognition_experiments/ \
		-e SPHINX_OPTS="${SPHINX_OPTS}" \
		${IMAGE_OWNER}/${SPHINX_IMAGE_NAME}:${SPHINX_VERSION}

sphinx-html-test: SPHINX_OPTS:=${SPHINX_OPTS} -b dummy
sphinx-html-test: sphinx-html

find-port-usage:
	sudo lsof -i -P -n | grep ${CHK_PORT}

debug-travis:
	curl -s -X POST \
		-H "Content-Type: application/json" \
		-H "Accept: application/json" -H "Travis-API-Version: 3" \
		-H "Authorization: token ${TRAVIS_TOKEN}" \
		-d '{ "quiet": true }' \
		https://api.travis-ci.com/job/${TRAVIS_JOB}/debug
