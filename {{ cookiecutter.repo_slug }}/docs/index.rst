.. cookiecutter-ds-docker documentation master file, created by
   sphinx-quickstart on Mon May 11 19:49:24 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


{{ cookiecutter.repo_name }}
==================================================

{{ cookiecutter.description }}

.. image:: https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}
    :alt: GitHub release (latest SemVer)
.. image:: https://readthedocs.org/projects/{{ cookiecutter.repo_slug }}/badge/?version=latest
    :target: https://{{ cookiecutter.repo_slug }}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}.svg?branch=master
    :target: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}r
.. image:: https://img.shields.io/codecov/c/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}
    :alt: Codecov
.. image:: https://img.shields.io/badge/License-AGPL%20v3-ff69b4.svg
    :target: http://www.gnu.org/licenses/agpl-3.0
.. image:: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg
    :target: http://creativecommons.org/licenses/by-nc-sa/4.0/

Quickstart
----------

In a terminal, run the following:

.. code:: bash

   make
   # once the docker stack is running, click the URL starting with
   # http://127.0.0.1:8888/?token=... to access JupyterLab
   #
   # mlflow UI is at http://localhost:5000/

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   overview
   setup
   run
   documentation
   test
   services
   license
   credits
   changelog

.. Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
