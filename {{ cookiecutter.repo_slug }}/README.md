# {{ cookiecutter.repo_name }}

{{ cookiecutter.description }}

![GitHub release (latest by date)](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}) [![Build Status](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}.svg?branch=master)](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}) [![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}) [![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-ff69b4.svg)](http://www.gnu.org/licenses/agpl-3.0) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Setup](#2-setup)
- [3. Running the Services](#3-running-the-services)
- [4. Testing and Development](#4-testing-and-development)
- [5. License](#5-license)
- [6. Authors](#6-authors)

## 1. Introduction

This project is based on [sertansenturk/cookiecutter-ds-docker](https://github.com/sertansenturk/cookiecutter-ds-docker). It consists of a docker-compose stack with the services below (See Sections [Setup](#setup) and [Running the Services](#running-the-services)):

1. A [Jupyter](https://jupyter.org/) service with minimal customization
2. An [mlflow](https://mlflow.org/) tracking server to store experiments
3. A [postgresql](https://www.postgresql.org/) database, which stores mlflow tracking information

We also include a Docker image for Python test and development (See [Section: Testing and Development](#testing-and-development)).

Typical commands to interact are wrapped in a `Makefile`. Below, we explain the common operations. For more options, please refer to the help by running on the terminal:

```bash
make help
```

## 2. Setup

To build the stack, run:

```bash
make build
```

If you need to make a clean start:

```bash
make clean-all
make build
```

This project installs a Python package called `{{ cookiecutter.package_name }}` to the Jupyter docker service, which located at [./src](src). By default, the package is "pip installed" in **editable** mode, and the **project's base folder is mounted** on the docker container so all changes are synchronized.

## 3. Running the Services

To start the stack with [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), run:

```bash
make
```

Note that the above commands also stops running stacks (if exist), cleans, and rebuilds the services to ensure that all everything is up-to-date.

By default, we base the Jupyter service on the official [scipy-notebook](https://hub.docker.com/r/jupyter/scipy-notebook/tags) image. You can also build & run from [tensorflow](https://hub.docker.com/r/jupyter/tensorflow-notebook/tags) or [pyspark](https://hub.docker.com/r/jupyter/pyspark-notebook/tags) notebooks by:

```bash
make tensorflow
make pyspark
```

If you want to use classic Jupyter notebooks, run instead:

```bash
make notebook
```

Once the service is running, you will see a link on the terminal, e.g., http://127.0.0.1:8888/?token=3c321..., which you can follow to access the notebook from your browser.

You can reach the mlflow UI at [http://localhost:5000](http://localhost:5000). For a simple example on how to track a run, please refer to [notebooks/mlflow_example.ipynb](notebooks/mlflow_example.ipynb)

## 4. Testing and Development

You can test the functionalities of the services (e.g., if `mlflow` logging functionality from the Jupyter service is correct) automatically by running the docker-compose stack in test mode. You can run the test stack locally by:

```bash
make test
```

We automate build, test, code style, and linting checks of the Python package, `./src/{{ cookiecutter.package_name }}` using `tox` in a docker environment. You can run `tox` by:

```bash
make tox
```

In addition, the repo has Travis CI integration enabled ([link](https://travis-ci.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }})). This service runs all of the checks mentioned above automatically after each push. Travis CI also generates code coverage reports for the Python package, which can be viewed on codecov ([link](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/)).

## 5. License

The source code hosted in this repository is licensed under [Affero GPL version 3](https://www.gnu.org/licenses/agpl-3.0.en.html). Any data (features, models,  figures, results, etc.) in this repository are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## 6. Authors

{{ cookiecutter.author_name }}  
{{ cookiecutter.author_email }}
