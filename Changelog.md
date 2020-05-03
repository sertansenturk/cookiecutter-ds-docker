# Changelog

## v0.8.0

- Increment `mlflow` version to 1.8.*
- Add Github issue and PR templates into the cookiecutter project

## v0.7.0

- Convert the repo into a [cookiecutter template](https://github.com/cookiecutter/cookiecutter)
- Rename the repo from *ds-template* to [cookiecutter-ds-docker](https://github.com/sertansenturk/cookiecutter-ds-docker)
- Fix a bug in `make test` where `mlflow` and `postgres` containers do not stop after testing
- Add maintainer and description related fields to `setup.py`

## v0.6.0

- Deprecate static Jupyter and no-cache builds
- Add git to python-dev docker image

## v0.5.0

- Add `scipy`, `tensorflow` and `pyspark` base image options from Jupyter docker stack
- Add pull request template

## v0.4.0

- Enable JupyterLab
- Pass username and id to the Jupyter service from the host
- Build and run improvements
- Add code of conduct

## v0.3.0

- Add [travis.ci](https://travis-ci.com/github/sertansenturk/cookiecutter-ds-docker) and [codecov](https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker/) integration

## v0.2.0

- Add Python template repo and Python `tox` automations
- Share host user uid & gid with the Postgres user in docker

## v0.1.0

- Create initial docker-compose stack with `Jupyter`, `mlflow` and `postgresql` images
