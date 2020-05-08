# cookiecutter-ds-docker

A Docker-based Data Science cookiecutter (for myself)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/sertansenturk/cookiecutter-ds-docker) [![Build Status](https://travis-ci.com/sertansenturk/cookiecutter-ds-docker.svg?branch=master)](https://travis-ci.com/sertansenturk/cookiecutter-ds-docker) [![codecov](https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker/branch/master/graph/badge.svg)](https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker) [![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-ff69b4.svg)](http://www.gnu.org/licenses/agpl-3.0) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Documentation](#2-documentation)
- [3. Quickstart](#3-quickstart)
- [4. License](#4-license)
- [5. Authors](#5-authors)

## 1. Introduction

This repo hosts a personalized, Docker-based [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template for Data Science projects. The template consists of a docker-compose stack with the services below:

1. A customized [Jupyter](https://jupyter.org/) service with a starter Python installed
2. An [mlflow](https://mlflow.org/) tracking server to store experiments
3. A [postgresql](https://www.postgresql.org/) database, which stores mlflow tracking information

- The template also includes a Docker image for Python test and development.

## 2. Documentation

Please refer to [Read The Docs](https://cookiecutter-ds-docker.readthedocs.io/en/latest/) for the documentation.

## 3. Quickstart

First, install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter) and [docker](https://docs.docker.com/get-docker/).

Then, run the commands below and follow the on-screen instructions to "bake" the template:

```bash
cd /[base_folder]
cookiecutter gh:sertansenturk/cookiecutter-ds-docker
```

To build and start the Docker stack in a baked project, run:

```bash
cd /[base_folder]/[repo_slug]
make
```

## 4. License

The source code hosted in this repository is licensed under [Affero GPL version 3](https://www.gnu.org/licenses/agpl-3.0.en.html). Any data (features, models,  figures, results, documentation, etc.) in this repository are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## 5. Authors

Sertan Şentürk  
contact@sertansenturk.com
