.. sectnum:: 
   :start: 6
   :depth: 1

Changelog
=========

v0.9.2
------
- Document permission issue when mounting NTFS drives in Linux (Pull Request `#55 <https://github.com/sertansenturk/cookiecutter-ds-docker/pull/55>`__)

v0.9.1
------

- Fix pip install Python package in editable mode
- `make clean-python` cleans `ipynb_checkpoints` folder(s)

v0.9.0
------

-  Add Sphinx documentation (Pull Requests `#36 <https://github.com/sertansenturk/cookiecutter-ds-docker/pull/36>`__, `#41 <https://github.com/sertansenturk/cookiecutter-ds-docker/pull/41>`__, `#45 <https://github.com/sertansenturk/cookiecutter-ds-docker/pull/45>`__, `#46 <https://github.com/sertansenturk/cookiecutter-ds-docker/pull/46>`__, `#49 <https://github.com/sertansenturk/cookiecutter-ds-docker/pull/49>`__)
-  Create online documentation at `Read the Docs <https://readthedocs.org/projects/cookiecutter-ds-docker/>`__
-  Create Sphinx docker image for local build and test (Pull Request `#43 <https://github.com/sertansenturk/cookiecutter-ds-docker/pull/43>`__)
-  Create cookiecutter docker image for local development (Pull Request `#39 <https://github.com/sertansenturk/cookiecutter-ds-docker/pull/39>`__)
-  Add VERSION file to the base folder
-  Add LICENSE file to the base folder (Pull Request `#33 <https://github.com/sertansenturk/cookiecutter-ds-docker/pull/33>`__)
-  Add ``step`` parameter to the ``mlflow.log_metrics`` test case and jupyter demo

v0.8.1
------

-  Fix docker stack start-up failure in Mac OSX (Pull Request `#31 <https://github.com/sertansenturk/cookiecutter-ds-docker/pull/31>`__)

v0.8.0
------

-  Increment ``mlflow`` version to 1.8.\*
-  Add Github issue and PR templates into the cookiecutter project
-  Simplify Jupyter multi-stage builds
-  Update ``cookiecutter`` installation instructions in the ``README.md``

v0.7.0
------

-  Convert the repo into a `cookiecutter template <https://github.com/cookiecutter/cookiecutter>`__
-  Rename the repo from *ds-template* to `cookiecutter-ds-docker <https://github.com/sertansenturk/cookiecutter-ds-docker>`__
-  Fix a bug in ``make test`` where ``mlflow`` and ``postgres`` containers do not stop after testing
-  Add maintainer and description related fields to ``setup.py``

v0.6.0
------

-  Deprecate static Jupyter and no-cache builds
-  Add git to python-dev docker image

v0.5.0
------

-  Add ``scipy``, ``tensorflow`` and ``pyspark`` base image options from Jupyter docker stack
-  Add pull request template

v0.4.0
------

-  Enable JupyterLab
-  Pass username and id to the Jupyter service from the host
-  Build and run improvements
-  Add code of conduct

v0.3.0
------

-  Add `travis.ci <https://travis-ci.com/github/sertansenturk/cookiecutter-ds-docker>`__ and `codecov <https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker/>`__ integration

v0.2.0
------

-  Add Python template repo and Python ``tox`` automation
-  Share host user uid & gid with the Postgres user in docker

v0.1.0
------

-  Create an initial docker-compose stack with ``Jupyter``, ``mlflow`` and ``postgresql`` images
