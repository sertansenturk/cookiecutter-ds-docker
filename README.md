# cookiecutter-ds-docker

A Docker-based Data Science cookiecutter

![GitHub release (latest by date)](https://img.shields.io/github/v/release/sertansenturk/cookiecutter-ds-docker) [![Build Status](https://travis-ci.com/sertansenturk/cookiecutter-ds-docker.svg?branch=master)](https://travis-ci.com/sertansenturk/cookiecutter-ds-docker) [![codecov](https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker/branch/master/graph/badge.svg)](https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker) [![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-ff69b4.svg)](http://www.gnu.org/licenses/agpl-3.0) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Setup](#2-setup)
- [3. Running a Baked Project](#3-running-a-baked-project)
- [4. Testing and Developing the Template](#4-testing-and-developing-the-template)
- [5. License](#5-license)
- [6. Authors](#6-authors)

## 1. Introduction

This repo hosts a personalized, Docker-based cookiecutter template for Data Science projects. The template consists of a docker-compose stack with the services below:

1. A [Jupyter](https://jupyter.org/) service with minimal customization. The Python package in the template is installed in this service.
2. An [mlflow](https://mlflow.org/) tracking server to store experiments.
3. A [postgresql](https://www.postgresql.org/) database, which stores mlflow tracking information.

The template also includes a Docker image for Python test and development.

Please refer to the [README.md file in the template folder](%7B%7B%20cookiecutter.repo_slug%20%7D%7D/README.md) for more information on the functionality.

## 2. Setup

First, you have to install `cookiecutter`. For example, you can install cookiecutter in Ubuntu or Mac by:

| OS              | Command                     |
| :-------------- | :-------------------------- |
| Ubuntu Linux    | `apt install cookiecutter`  |
| Mac OSX         | `brew install cookiecutter` |

For other methods to install `cookiecutter`, please refer to the [official documentation](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter).

Then, "baking" the template is straightforward:

```bash
cd /[base_folder]
cookiecutter https://github.com/sertansenturk/cookiecutter-ds-docker
```

*cookiecutter* will ask you to fill a few variables, namely:

| Variable        | Explanation                                    | Modifies |
| :-------------- | :--------------------------------------------  | :- |
| repo_name       | Name of the repository                         | Header of `README.md` |
| repo_slug       | Slug of the repository name                    | Repository folder name, GitHub URL, explanations in `README.md` |
| package_name    | Name of the Python package in the project      | Python package name, `setup.py`, `tox.ini`, unittests, docker image names, explanations in `README.md` |
| author_name     | Name of the authoring person/team/organization | author name in `setup.py` and `README.md` |
| author_email    | E-mail to contact the author                   | author e-mail in `setup.py`, `CODE_OF_CONDUCT.md` and `README.md` |
| github_username | Github username                                | GitHub URL, URLs in `setup.py`, docker image names, explanations in `README.md` |
| description     | A short description of the project             | explanations in `setup.py` and `README.md` |

Afterward, the project will be created in `/[base_folder]/[repo_slug]`.

For additional command line options and information about Python cookiecutter, please refer to [official cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/advanced/cli_options.html#command-line-options).

## 3. Running a Baked Project

To build and run the Docker stack in a baked project, simply run:

```bash
cd /[base_folder]/[repo_slug]
make
```

Please refer to the [README.md file in the template folder](%7B%7B%20cookiecutter.repo_slug%20%7D%7D/README.md) for other commands.

## 4. Testing and Developing the Template

You can test the cookiecutter, the baked services, and the Python package (e.g., build, unittest, code style, linting) locally by:

```bash
make test
```

This repo also has Travis CI integration enabled ([link](https://travis-ci.com/github/sertansenturk/cookiecutter-ds-docker)). This service automatically runs all of the checks mentioned above after each push. Travis CI also generates code coverage reports for the Python package, which you can view on codecov ([link](https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker/)).

## 5. License

The source code hosted in this repository is licensed under [Affero GPL version 3](https://www.gnu.org/licenses/agpl-3.0.en.html). Any data (features, models,  figures, results, etc.) in this repository are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## 6. Authors

Sertan Şentürk  
contact@sertansenturk.com
