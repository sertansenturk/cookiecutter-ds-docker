*****************************************
Overview
*****************************************

Docker
=========================================

``{{ cookiecutter.repo_slug }}`` consists of a docker-compose stack with the services below:

1. A customized `Jupyter <https://jupyter.org/>`__ service with a starter Python package installed. Comes with *Python 3.7*.
2. An `mlflow <https://mlflow.org/>`__ tracking server to log experiments.
3. A `postgresql <https://www.postgresql.org/>`__ database, which stores *mlflow* tracking information.

We mount several folders from our host to these services:

- The project base folder, ``./``, is mounted on the *Jupyter docker* container so that all modifications are synchronized immediately.
- The folder, ``./data/artifacts``, where the artifacts logged by *mlflow* are stored by default, is mounted on the *Jupyter* and *mlflow* services.
- The *postgresql data folder*, ``/var/lib/postgresql/data`` inside the container, is mounted locally on ``./data/db/`` to keep the database intact, after stopping the stack.

.. note::
   The project also includes these supplementary, standalone *Docker* images:

   1. for building Sphinx documentation (See `Documentation <documentation.html>`__)
   2. for testing *Python* code (See `Python Tests <testing.html/#python>`__)

Python
=========================================

The project comes with a Python starter package called ``{{ cookiecutter.package_name }}``, which is located at ``./src/``. The package is ``pip`` installed to the *Jupyter docker* service in **editable** mode.

Makefile
=========================================

``Makefile`` commands are used extensively to work with ``{{ cookiecutter.repo_slug }}``. For all commands, please refer to the help by running on the terminal:

.. code:: bash

   make help
