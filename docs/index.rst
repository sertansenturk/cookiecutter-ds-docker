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
   
``cookiecutter-ds-docker`` is a personalized, Docker-based cookiecutter template repo for Data Science projects. It aims to standardize the common decisions (repo structure, setup, integrations, etc.), which I need to consider for each new project, and hence minimize the (overtly dull) start-up effort for future work.

Quickstart
----------

In a terminal, run the following:

.. code:: bash

   cd {base_folder}
   cookiecutter gh:sertansenturk/cookiecutter-ds-docker
   # follow the on-screen instructions to cut the project
   # ...
   cd {{ cookiecutter.repo_slug}} # replace repo_slug with what you entered earlier
   make
   # once the docker stack is running, click the URL starting with 
   # http://127.0.0.1:8888/?token=... to access JupyterLab
   # mlflow UI is at http://localhost:5000/

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   template
   project
   license
   credits
   changelog

.. Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
