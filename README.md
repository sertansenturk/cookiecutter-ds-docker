# ds-template

A personalized Github template repository for data science projects

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-ff69b4.svg)](http://www.gnu.org/licenses/agpl-3.0) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

Currently, the template consists of a docker-compose stack with the services below:

1. A [Jupyter notebook](https://jupyter.org/) with minimal customization
2. An [mlflow](https://mlflow.org/) tracking server to store experiments
3. A [postgresql](https://www.postgresql.org/) database, which stores mlflow tracking information

In addition, we include the Docker images below for utility's sake:

1. A Python development image to facilitate code test and development in Python

The common use cases to interact with template are wrapped in a `Makefile`. Below, we explain the typical operations. For more options, please refer to the help by running on the terminal:

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

**Note:** You may need to grant sudo permissions for `make clean-all`

## Run the Services

To start the stack, run:

```bash
make run
```

Once the service is running, you will see a link, e.g. http://127.0.0.1:8888/?token=3c321..., which you can follow to access the notebook from your browser.

You can access the mlflow UI at [http://localhost:5000](http://localhost:5000). For an simple example on how to track a "run," please refer to [notebooks/mlflow_test.py](notebooks/mlflow_test.ipynb)

## Test and Development

The repo includes a starting Python package at [src/template_repo](src/template_repo), which has the installation, testing, and linting set. We automate these checks using `tox`, which can be run by:

```bash
make tox
```

## License

The source code hosted in this repository is licenced under [Affero GPL version 3](https://www.gnu.org/licenses/agpl-3.0.en.html). Any data (features, models,  figures, results etc.) in this repository are licenced under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## Authors

Sertan Şentürk
contact@sertansenturk.com
