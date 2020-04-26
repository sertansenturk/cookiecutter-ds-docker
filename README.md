# cookiecutter-ds-docker

A Docker-based Data Science cookiecutter

![GitHub release (latest by date)](https://img.shields.io/github/v/release/sertansenturk/cookiecutter-ds-docker) [![Build Status](https://travis-ci.com/sertansenturk/cookiecutter-ds-docker.svg?branch=master)](https://travis-ci.com/sertansenturk/cookiecutter-ds-docker) [![codecov](https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker/branch/master/graph/badge.svg)](https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker) [![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-ff69b4.svg)](http://www.gnu.org/licenses/agpl-3.0) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Setup](#2-setup)
- [3. Running the Services](#3-running-the-services)
- [4. Testing and Development](#4-testing-and-development)
- [5. License](#5-license)
- [6. Authors](#6-authors)

## 1. Introduction

This repo hosts a personalized, Docker-based Data Science cookiecutter template. The template consists of a docker-compose stack with the services below:

1. A [Jupyter](https://jupyter.org/) service with minimal customization
2. An [mlflow](https://mlflow.org/) tracking server to store experiments
3. A [postgresql](https://www.postgresql.org/) database, which stores mlflow tracking information

In addition, it also includes a Docker image for Python test and development.

Please refer to the [README.md file in the template folder]({{ cookiecutter.repo_slug }}/README.md) for additional information on the template's functionalities.

## 2. Setup

First, you have to [install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter). For example, you can install cookiecutter in a [virtualenv](https://virtualenv.pypa.io/en/stable/) by:

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install cookiecutter
```

Then, baking a template is straightforward:

```bash
cd /path/to/base/folder
cookiecutter https://github.com/sertansenturk/cookiecutter-ds-docker
```



For more options and general information about Python cookiecutter, please refer to the [official cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/).

## 4. Testing and Development

You can test the functionalities of the services (e.g., if `mlflow` logging functionality from the Jupyter service is correct) automatically by running the docker-compose stack in test mode. You can run the test stack locally by:

```bash
make test
```

We automate build, test, code style, and linting checks of the Python package, `./src/{{ cookiecutter.package_name }}` using `tox` in a docker environment. You can run `tox` by:

```bash
make tox
```

In addition, the repo has Travis CI integration enabled ([link](https://travis-ci.com/github/sertansenturk/cookiecutter-ds-docker)). This service runs all of the checks mentioned above automatically after each push. Travis CI also generates code coverage reports for the Python package, which can be viewed on codecov ([link](https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker/)).

## 5. License

The source code hosted in this repository is licensed under [Affero GPL version 3](https://www.gnu.org/licenses/agpl-3.0.en.html). Any data (features, models,  figures, results, etc.) in this repository are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## 6. Authors

Sertan Şentürk  
contact@sertansenturk.com
