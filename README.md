# ds-template

A personalized Github template repository for data science projects

![GitHub release (latest by date)](https://img.shields.io/github/v/release/sertansenturk/ds-template) [![Build Status](https://travis-ci.com/sertansenturk/ds-template.svg?branch=master)](https://travis-ci.com/sertansenturk/ds-template) [![codecov](https://codecov.io/gh/sertansenturk/ds-template/branch/master/graph/badge.svg)](https://codecov.io/gh/sertansenturk/ds-template) [![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-ff69b4.svg)](http://www.gnu.org/licenses/agpl-3.0) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

Currently, the template consists of a docker-compose stack with the services below:

1. A [Jupyter notebook](https://jupyter.org/) with minimal customization
2. An [mlflow](https://mlflow.org/) tracking server to store experiments
3. A [postgresql](https://www.postgresql.org/) database, which stores mlflow tracking information

In addition, we include the Docker images below for utility's sake:

1. A Python development image to facilitate code test and development in Python

Commands to interact with template are wrapped in a `Makefile`. Below, we explain the common operations. For more options, please refer to the help by running on the terminal:

```bash
make help
```

## Setup

To build the stack, simply run:

```bash
make build
```

If you need to make a clean start:

```bash
make clean-all
make build
```

This repo also includes a template Python package at [src/python_package](src/python_package), which is installed to the Jupyter docker image. By default, the package is "pip installed" in **editable** mode and the **base folder is mounted** on the docker container so that the changes in the code are synchronized.

If you want to install the package statically, instead of `make build`, execute:

```bash
make build-static
```

## Run the Services

To start the stack, run:

```bash
make
```

Note that the above command also stops running stacks (if exist), cleans, and rebuilds the services to ensure that all everything starts up-to-date.

If you want to run the stack with the Python package installed statically, run instead:

```bash
make static
```

Once the service is running, you will see a link on the terminal, e.g. http://127.0.0.1:8888/?token=3c321..., which you can follow to access the notebook from your browser.

You can reach the mlflow UI at [http://localhost:5000](http://localhost:5000). For an simple example on how to track a run, please refer to [notebooks/mlflow_example.ipynb](notebooks/mlflow_example.ipynb)

## Test and Development

We can test the functionalities of the services (e.g. if `mlflow` handles logging correctly from the Jupyter service) automatically by running the docker-compose stack in test mode. You can run the test stack locally by:

```bash
make test
```

We automate build, test, code style and linting checks of the template Python package using `tox` in a docker environment. You can run `tox` locally by:

```bash
make tox
```

In addition, the repo has Travis CI integration ([link](https://travis-ci.com/github/sertansenturk/ds-template)), where we make the aferomentioned checks automatically after each push. Travis CI also generates unittest code coverage reports for the Python package, which can be checked on codecov ([link](https://codecov.io/gh/sertansenturk/ds-template/)).

## License

The source code hosted in this repository is licenced under [Affero GPL version 3](https://www.gnu.org/licenses/agpl-3.0.en.html). Any data (features, models,  figures, results etc.) in this repository are licenced under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## Authors

Sertan Şentürk
contact@sertansenturk.com
