# {{ cookiecutter.repo_name }}

{{ cookiecutter.description }}

![GitHub release (latest by date)](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}) [![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.repo_slug }}/badge/?version=latest)](https://{{ cookiecutter.repo_slug }}.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}.svg?branch=master)](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}) [![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}) [![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-ff69b4.svg)](http://www.gnu.org/licenses/agpl-3.0) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Documentation](#2-documentation)
- [3. Quickstart](#3-quickstart)
- [4. License](#4-license)
- [5. Authors](#5-authors)

## 1. Introduction

This project is "cut" from [sertansenturk/cookiecutter-ds-docker](https://github.com/sertansenturk/cookiecutter-ds-docker). It consists of a docker-compose stack with the services below (See Sections [Setup](#setup) and [Running the Services](#running-the-services)):

1. A [Jupyter](https://jupyter.org/) service with minimal customization
2. An [mlflow](https://mlflow.org/) tracking server to store experiments
3. A [postgresql](https://www.postgresql.org/) database, which stores mlflow tracking information

- The template also includes a *Docker* image for local *Python* test and development, and another for building local *Sphinx* documentation.

## 2. Documentation

Please refer to [Read The Docs](https://{{ cookiecutter.repo_slug }}.readthedocs.io) for the documentation.

## 3. Quickstart

To build and start the Docker stack, run:

```bash
make
```

## 4. License

The source code hosted in this repository is licensed under [Affero GPL version 3](https://www.gnu.org/licenses/agpl-3.0.en.html). Any data (features, models,  figures, results, documentation, etc.) in this repository are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## 5. Authors

{{ cookiecutter.author_name }}  
{{ cookiecutter.author_email }}
