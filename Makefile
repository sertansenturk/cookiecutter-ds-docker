SHELL := /bin/bash
.DEFAULT_GOAL := default
.PHONY: \
	help default cut \
	clean clean-test clean-$(DOCS_FOLDER) \
	test sphinx-html-test \
	cookiecutter-build sphinx-build \
	sphinx-quickstart sphinx-html \
	debug-travis

HELP_PADDING = 28
bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)
padded_str := %-$(HELP_PADDING)s
pretty_command := $(bold)$(padded_str)$(sgr0)

VENV_INTERP = python3
VENV_NAME ?= venv

BUILDKIT = 1
DOCKER_USERNAME = sertansenturk

MAKEFILE_DIR = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

CUT_BASE_FOLDER = ..
CUT_TMP_FOLDER = tmp
CUT_OPTS :=

TEST_BASE_FOLDER = .
TEST_FOLDER = test-project

COOKIECUTTER_VERSION = latest
COOKIECUTTER_IMAGE = $(DOCKER_USERNAME)/cookiecutter:$(COOKIECUTTER_VERSION)

DOCS_FOLDER = docs
SPHINX_VERSION = 3.0.3
SPHINX_IMAGE = $(DOCKER_USERNAME)/sphinx:$(SPHINX_VERSION)
SPHINX_OPTS := -nWT -b linkcheck --keep-going

# default port to free using free-port, default: 5432 (postgres)
PORT = 5432

TRAVIS_JOB =
TRAVIS_TOKEN =

help:
	@printf "======= General ======\n"
	@printf "$(pretty_command): alias of \"make cut\" (see below)\n" \(default\)
	@printf "$(pretty_command): cut a new project\n" cut
	@printf "$(padded_str)CUT_OPTS, cookiecutter options (default: $(CUT_OPTS))\n"
	@printf "$(pretty_command): run cookiecutter, template, and documentation tests\n" test
	@printf "\n"
	@printf "======= Setup =======\n"
	@printf "$(pretty_command): create a python virtualenv called $(VENV_NAME)\n" $(VENV_NAME)
	@printf "$(padded_str)VENV_INTERP, python interpreter (default: $(VENV_INTERP))\n"
	@printf "$(pretty_command): install cookiecutter in the virtualenv\n" install
	@printf "\n"
	@printf "======= Cleanup ======\n"
	@printf "$(pretty_command): remove everything described below\n" clean
	@printf "$(pretty_command): remove the test project folder\n" clean-test
	@printf "$(pretty_command): remove the virtualenv\n" clean-$(VENV_NAME)
	@printf "$(pretty_command): remove the sphinx documentation\n" clean-$(DOCS_FOLDER)
	@printf "\n"
	@printf "======= Documentation ======\n"
	@printf "$(pretty_command): builds sphinx docker image\n" sphinx-build
	@printf "$(pretty_command): \"quickstarts\" sphinx documentation\n" sphinx-quickstart
	@printf "$(pretty_command): cleans the documentation at \"./docs/_build/\"\n" sphinx-clean
	@printf "$(pretty_command): builds sphinx html docs at \"./docs/_build/html\"\n" sphinx-html
	@printf "$(padded_str)SPHINX_OPTS, options to pass to sphinx (default: $(SPHINX_OPTS))\n"
	@printf "$(pretty_command): tests sphinx html build\n" sphinx-html-test
	@printf "\n"
	@printf "========= Misc =======\n"
	@printf "$(pretty_command): kill applications, which are bound to the given port. Useful for freeing ports from phantom tasks\n" free-port
	@printf "$(padded_str)PORT, Port to check (default: $(PORT))\n"
	@printf "$(pretty_command): send a job debug request to travis\n" debug-travis
	@printf "$(padded_str)TRAVIS_TOKEN, travis api token (default: $(TRAVIS_TOKEN))\n"
	@printf "$(padded_str)TRAVIS_JOB, travis job id (default: $(TRAVIS_JOB))\n"

default: cut

clean: clean-$(VENV_NAME) clean-test clean-$(DOCS_FOLDER)

clean-test:
	rm -rf $(TEST_FOLDER)

clean-$(DOCS_FOLDER):
	rm -rf $(DOCS_FOLDER)

cookiecutter-build:
	DOCKER_BUILDKIT=$(BUILDKIT) \
	docker build . \
		-f ./docker/cookiecutter/Dockerfile \
		-t $(COOKIECUTTER_IMAGE)

cut: cookiecutter-build
	mkdir -p $(CUT_TMP_FOLDER)
	docker run \
		-it --rm \
		-v $(MAKEFILE_DIR):/project \
		-e CUT_OPTS="$(CUT_OPTS)" \
		$(COOKIECUTTER_IMAGE)
	find $(CUT_TMP_FOLDER)/ -maxdepth 1 -type d -not -name $(CUT_TMP_FOLDER) \
		-exec mv {} $(CUT_BASE_FOLDER)/ \;
	rm -rf $(CUT_TMP_FOLDER)

test: CUT_BASE_FOLDER:=$(TEST_BASE_FOLDER)
test: CUT_OPTS:=--no-input repo_slug=$(TEST_FOLDER)
test: sphinx-html-test clean-test cut
	cd $(TEST_FOLDER) ; \
	make test ; \
	make tox
	$(MAKE) clean-test

sphinx-build:
	DOCKER_BUILDKIT=$(BUILDKIT) \
	docker build \
		--build-arg SPHINX_VERSION=$(SPHINX_VERSION) \
		. \
		-f ./docker/sphinx/Dockerfile \
		-t $(SPHINX_IMAGE)

sphinx-quickstart: sphinx-build
	mkdir -p $(DOCS_FOLDER)
	docker run -it --rm\
		-v $(MAKEFILE_DIR):/repo/ $(SPHINX_IMAGE) \
		sphinx-quickstart

sphinx-clean: sphinx-build
	docker run -it --rm \
		-v $(MAKEFILE_DIR):/repo/ \
		$(SPHINX_IMAGE) \
		make clean

sphinx-html: sphinx-clean
	docker run -it --rm \
		-v $(MAKEFILE_DIR):/repo/ \
		-e SPHINX_OPTS="$(SPHINX_OPTS)" \
		$(SPHINX_IMAGE)

sphinx-html-test: SPHINX_OPTS:=$(SPHINX_OPTS) -b dummy
sphinx-html-test: sphinx-html

free-port:
	sudo lsof -i -P -n | grep ${PORT} | awk '{ print $$2 }' | xargs sudo kill

debug-travis:
	curl -s -X POST \
		-H "Content-Type: application/json" \
		-H "Accept: application/json" -H "Travis-API-Version: 3" \
		-H "Authorization: token $(TRAVIS_TOKEN)" \
		-d '{ "quiet": true }' \
		https://api.travis-ci.com/job/$(TRAVIS_JOB)/debug
