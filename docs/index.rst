.. cookiecutter-ds-docker documentation master file, created by
   sphinx-quickstart on Fri May  8 15:23:16 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

cookiecutter-ds-docker
==================================================

*A Docker-based Data Science cookiecutter (for myself)*

.. image:: https://img.shields.io/github/v/release/sertansenturk/cookiecutter-ds-docker
    :alt: GitHub release (latest SemVer)
.. image:: https://travis-ci.com/sertansenturk/cookiecutter-ds-docker.svg?branch=master
    :target: https://travis-ci.com/sertansenturk/cookiecutter-ds-docker
.. image:: https://img.shields.io/codecov/c/github/sertansenturk/cookiecutter-ds-docker
    :alt: Codecov
.. image:: https://img.shields.io/badge/License-AGPL%20v3-ff69b4.svg
    :target: http://www.gnu.org/licenses/agpl-3.0
.. image:: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg
    :target: http://creativecommons.org/licenses/by-nc-sa/4.0/
   
``cookiecutter-ds-docker`` is a personalized, Docker-based cookiecutter template repo for Data Science projects. The template consists of a docker-compose stack with the services below:

1. A customized `Jupyter <https://jupyter.org/>`__ service with a starter Python package installed
2. An `mlflow <https://mlflow.org/>`__ tracking server to store experiments
3. A `postgresql <https://www.postgresql.org/>`__ database, which stores mlflow tracking information

The template also includes a Docker image for Python test and development.

Please refer to the ``{{ cookiecutter.repo_slug}}/README.md`` file for more information on the functionality.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   setup
   quickstart
   testing
   documentation

License
----------

The source code is licensed under `Affero GPL version 3 <https://www.gnu.org/licenses/agpl-3.0.en.html>`_. Any data (features, models, figures, results, documentation, etc.) are licensed under `Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-nc-sa/4.0/>`_.

Authors
----------

Sertan Şentürk - contact@sertansenturk.com

.. Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
