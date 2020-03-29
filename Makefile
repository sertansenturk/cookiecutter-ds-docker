#!make
SHELL := /bin/bash
.DEFAULT_GOAL := default
.PHONY: \
	help default all all-no-cache \
	purge clean clean-all clean-store \
	prune build build-no-cache up down down-all 

HELP_PADDING = 28
bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)
padded_str := %-$(HELP_PADDING)s
pretty_command := $(bold)$(padded_str)$(sgr0)

include ./docker/.env  # environmen variables used in docker

PRUNE_OPTS = -f

BUILD_OPTS = 
BUILD_ALL_OPTS = --no-cache

DOWN_OPTS = --remove-orphans
DOWN_ALL_OPTS = ${DOWN_OPTS} --rmi all -v

UP_OPTS =

help:
	@printf "======= General ======\n"
	@printf "$(pretty_command): run \"all\" (see below)\n" \(default\)
	@printf "$(pretty_command): run \"clean\", \"build\", and \"up\"\n" all
	@printf "$(pretty_command): run \"clean-all\", \"build-no-cache\", and \"up\"\n" all-no-cache
	@printf "\n"
	@printf "======= Cleanup ======\n"
	@printf "$(pretty_command): run \"down\", \"prune\", and \"clean-store\"\n" clean
	@printf "$(pretty_command): run \"down-all\", \"prune\", and \"clean-store\"\n" clean-all
	@printf "$(pretty_command): remove local folders mounted as volumes in docker-compose\n" clean-store
	@printf "$(pretty_command): alias of \"clean-all\"\n" purge
	@printf "\n"
	@printf "======= Docker =======\n"
	@printf "$(pretty_command): build the docker-compose stack\n" build
	@printf "$(padded_str)BUILD_OPTS, \"docker-compose build\" options (default: $(BUILD_OPTS))\n"
	@printf "$(pretty_command): build docker-compose stack with ${BUILD_ALL_OPTS} option(s)\n" build-no-cache
	@printf "$(pretty_command): start the docker-compose stack\n" up
	@printf "$(padded_str)UP_OPTS, \"docker-compose up\" options (default: $(UP_OPTS))\n"
	@printf "$(pretty_command): stop the docker-compose stack and remove artifacts created by \"up\"\n" down
	@printf "$(padded_str)DOWN_OPTS, \"docker-compose down\" options (default: $(DOWN_OPTS))\n"
	@printf "$(pretty_command): build docker-compose stack with ${DOWN_ALL_OPTS} option(s)\n" down-all

default: all

all: clean build up
all-no-cache: clean-all build-no-cache up

purge: clean-all
clean-all: down-all prune clean-store
clean: down prune clean-store 
clean-store:
	rm -rf ${MLFLOW_ARTIFACT_STORE} ${POSTGRES_STORE}

prune:
	docker system prune ${PRUNE_OPTS}

build: 
	docker-compose build ${BUILD_OPTS}

build-no-cache: BUILD_OPTS:=$(BUILD_ALL_OPTS)
build-no-cache: build

up: 
	mkdir -p ${MLFLOW_ARTIFACT_STORE} ${POSTGRES_STORE}; \
	docker-compose up ${UP_OPTS}

down:
	docker-compose down ${DOWN_OPTS}
down-all: DOWN_OPTS := ${DOWN_ALL_OPTS}
down-all: down
