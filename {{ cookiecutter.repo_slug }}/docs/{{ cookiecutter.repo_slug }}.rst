.. sectnum:: :start: 2

#########################################
{{ cookiecutter.repo_slug }}
#########################################

*****************************************
Overview
*****************************************

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

   1. for building Sphinx documentation (See `Documentation <#documentation>`__)
   2. for *Python* test and development (See `Python Tests <#python>`__)

Python development
=========================================

The project comes with a Python starter package called ``{{ cookiecutter.package_name }}``, which is located at ``./src/``. The package is ``pip`` installed to the *Jupyter docker* service in **editable** mode, while `the Docker stack is being built <#setup>`_.

Makefile
=========================================

Below, we introduce some useful ``Makefile`` commands to interact with the project. For all commands, please refer to the help by running on the terminal:

.. code:: bash

   make help

*****************************************
Setup
*****************************************

If you want to build the stack from the cut project without starting it, run:

.. code:: bash

   make build

The above command will build these images:

.. +-----------------------+------------------------------------------------------------------------------------+
   | Service               | Image name                                                                         |
   +=======================+====================================================================================+
   | *jupyter*             | ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/jupyter:0.1.0``  |
   +-----------------------+------------------------------------------------------------------------------------+
   | *mlflow*              | ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/mlflow:0.1.0``   |
   +-----------------------+------------------------------------------------------------------------------------+
   | *postgres*            | ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/postgres:0.1.0`` |
   +-----------------------+------------------------------------------------------------------------------------+

.. note::

   The version tag of docker images in a new project starts from ``0.1.0``, which is read from the ``VERSION`` variable in ``.env`` file.

If you need to make a clean start:

.. code:: bash

   make clean-all

*****************************************
Running the Docker Stack
*****************************************

To build and run the Docker stack in a cut project, run:

.. code:: bash

   make

For convenience, the above command stops running stacks (if exist), cleans, (re)builds, and starts the services.

.. note:: **Accessing Jupyter UI**

   Once the stack is up and running, you will see a link on the terminal, e.g., ``http://127.0.0.1:8888/?token=3c321...``, which you can follow to access the *JupyterLab* interface from your browser.

.. note:: **Accessing mlflow UI**

   You can reach the *mlflow* UI at ``http://localhost:5000``. For a simple example on how to track a run, please refer to `notebooks/mlflow\_example.ipynb <https://github.com/sertansenturk/cookiecutter-ds-docker/blob/master/%7B%7B%20cookiecutter.repo_slug%20%7D%7D/notebooks/mlflow_example.ipynb>`__.

   For in-depth tutorials, please refer to the `official mlflow documentation <https://mlflow.org/docs/latest/tutorials-and-examples/index.html>`__.

Additional Run Options
=========================================

By default, we base the *Jupyter* service on the official `scipy-notebook <https://hub.docker.com/r/jupyter/scipy-notebook/tags>`__ image. You can also build & run from `tensorflow <https://hub.docker.com/r/jupyter/tensorflow-notebook/tags>`__ or `pyspark <https://hub.docker.com/r/jupyter/pyspark-notebook/tags>`__ notebooks by:

.. code:: bash

   make tensorflow
   make pyspark

If you want to use classic *Jupyter* notebooks, run instead:

.. code:: bash

   make notebook

*****************************************
Documentation
*****************************************

The project comes with a basic documentation, which is located at ``{{ cookiecutter.repo_slug }}/docs``. You can use `Sphinx <https://www.sphinx-doc.org>`__ to build the documentation locally:

.. code:: bash

   make sphinx-html

The above command builds a docker image called ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/sphinx`` and runs a container from the image, which -in turn- builds the documentation. Then, you can then access the documentation by opening ``{{ cookiecutter.repo_slug }}/docs/_build/html/index.html`` on your browser.

.. note ::

   You may want to host the documentation online, e.g. at `Read the Docs <https://readthedocs.io>`__ or `Github Pages <https://pages.github.com/>`__, especially if you host the project in *Github*. Please refer to these services to learn how.

To validate the documentation without building, run:

.. code:: bash

   make sphinx-html-test

.. note ::
   
   If you `enable Travis CI integration <#running-tests-in-travis-ci>`__, the documentation is validated automatically.

*****************************************
Testing
*****************************************

Python
=========================================

Build, code style, linting checks and unittests of the starter Python package are automated using ``tox`` in a docker environment. You can run these tests by:

.. code:: bash

   make tox

This command builds a *docker* image called ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/python-dev``, and runs the Python tests inside a container.

Docker Stack
=========================================

You can test the integration of the Docker services (e.g., sending log requests to *mlflow tracking server* from the *Jupyter* service) automatically by running the *docker-compose* stack in "test" mode by executing:

.. code:: bash

   make test

Running Tests in Travis CI
=========================================

The cut project comes with *Travis CI* integration. 

.. important ::

   For *Travis CI* to function, you need to push the project into *Github* with the same ``{{ cookiecutter.github_username }}`` and ``{{ cookiecutter.repo_slug }}``, and grant *Travis CI* access to the repository.
   
   Please follow the `official Travis CI documentation <https://docs.travis-ci.com/user/tutorial/>`_ for instructions.

*Travis CI* runs all of the checks mentioned above automatically after each push, which could be viewed at:
 
``https://travis-ci.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}``

It also generates code coverage reports for the starter Python package, which can be viewed at codecov: 

``https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/``
