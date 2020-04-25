# Changelog

## v0.6.0

- Converted into [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- Renamed the repo to [cookiecutter-ds-docker](https://github.com/sertansenturk/cookiecutter-ds-docker)
- Fixed a bug in `make test` where `mlflow` and `postgres` containers do not stop after testing
- Deprecate static Jupyter and no-cache builds
- Added git to python-dev docker image

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
