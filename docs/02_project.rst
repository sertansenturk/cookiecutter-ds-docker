.. sectnum:: :start: 2

#########################################
Working with a Project
#########################################

.. attention::

   We assume you have already `cut a project by following the instructions <01_cookiecutter_template.html#cutting-a-new-project>`__, and you are in the project directory, ``/{ base_folder }/{{ cookiecutter.repo_slug }}``.

*****************************************
Overview
*****************************************

A project cut from ``cookiecutter-ds-docker`` consists of a docker-compose stack with the services below:

1. A customized `Jupyter <https://jupyter.org/>`__ service with a starter Python package installed. It runs on *Python 3.7*.
2. An `mlflow <https://mlflow.org/>`__ tracking server to log experiments.
3. A `postgresql <https://www.postgresql.org/>`__ database, which stores *mlflow* tracking information.

We mount several folders from our host to these services:

- The project base folder, ``./``, is mounted on the *Jupyter docker* container so that all modifications are synchronized immediately.
- The folder, ``./data/artifacts``, where the artifacts logged by *mlflow* are stored by default, is mounted on the *Jupyter* and *mlflow* services.
- The *postgresql data folder*, ``/var/lib/postgresql/data`` inside the container, is mounted locally on ``./data/db/`` to keep the database intact, after stopping the stack.

.. note::
   The project also includes these supplementary, standalone *Docker* images:

   1. for building Sphinx documentation (See `Documentation <#documentation>`__)
   2. for testing *Python* code (See `Python Tests <#python>`__)

Makefile
=========================================

``Makefile`` commands are used extensively to interact with the project. For a list of commands, please refer to the help by running on the terminal:

.. code:: bash

   make help

Python development
=========================================

The project comes with a Python starter package called ``{{ cookiecutter.package_name }}``, which is located at ``./src/``. The package is ``pip`` installed to the *Jupyter docker* service in **editable** mode, while `the Docker stack is being built <#setup>`_.

*****************************************
Setup
*****************************************

If you want to build the stack from the cut project without starting it, run:

.. code:: bash

   make build

The above command will build these images:

+-----------------------+------------------------------------------------------------------------------------+
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

By default, the *Jupyter* service is based on the official `scipy-notebook <https://hub.docker.com/r/jupyter/scipy-notebook/tags>`__ image. You can also build & run from `tensorflow <https://hub.docker.com/r/jupyter/tensorflow-notebook/tags>`__ or `pyspark <https://hub.docker.com/r/jupyter/pyspark-notebook/tags>`__ notebooks by:

.. code:: bash

   make tensorflow
   make pyspark

If you want to use classic *Jupyter* notebooks, run instead:

.. code:: bash

   make notebook

*****************************************
Documentation
*****************************************

The project comes with basic documentation, which is located at ``{{ cookiecutter.repo_slug }}/docs``. You can use `Sphinx <https://www.sphinx-doc.org>`__ to build the documentation locally by running:

.. code:: bash

   make sphinx-html

The above command builds a docker image called ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/sphinx``. It then starts a container from the image and renders the documentation (including automatic Python API documentation from docstrings).

Afterward, you can access the documentation by opening ``./docs/_build/html/index.html`` on your browser.

.. note::

   By default, ``{{ cookiecutter.package_name }}`` follows the `numpy docstring style <https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard>`__. If you would like to use `Google style docstrings <https://google.github.io/styleguide/pyguide.html>`__ instead, please reverse the ``napoleon_google_docstring`` and ``napoleon_numpy_docstring`` variables inside ``{{ cookiecutter.repo_slug }}/docs/conf.py``.

*****************************************
Testing
*****************************************

Python
=========================================

Build, code style, linting checks and unittests of the starter Python package are automated using ``tox`` in a docker environment. You can run these tests by:

.. code:: bash

   make tox

This command builds a *docker* image called ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/python-dev``. It then starts a container from the image and runs the Python tests.

Docker Stack
=========================================

You can test the integration of the Docker services (e.g., sending log requests to *mlflow tracking server* from the *Jupyter* service) automatically by running the *docker-compose* stack in "test" mode by executing:

.. code:: bash

   make test

Documentation
=========================================

To validate the documentation without building, run:

.. code:: bash

   make sphinx-html-test

*****************************************
Online Services
*****************************************

Github
=========================================

*Github* is a popular code hosting platform with `(git) version control <https://git-scm.com/>`__ (and many other complementary services).

To host the project in *Github*, follow the steps below:

1. Create an **empty** repository (**do not** initialize *readme*, *license*, or *.gitignore* files). See the `official Github documentation <https://help.github.com/en/github/getting-started-with-github/create-a-repo>`__ for detailed instructions.

   .. note::

      Your *Github Username* and *Repository Name* should match ``{{ cookiecutter.github_username }}`` and ``{{ cookiecutter.repo_slug }}``, respectively.

2. Initialize git and make the first commit, e.g.:

   .. code::

      git init
      git add .
      git commit -m "First commit"

3. Push the project to *Github*, e.g. using *https* connection:  

   .. code::

      git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}.git
      git push -u origin master

For more information on the *Github ecosystem*, please refer to the official `help <https://help.github.com/en>`__ and `guides <https://guides.github.com/>`__.

Travis CI
=========================================

*Travis CI* is a continuous integration service to build and test projects hosted in *Github*. The project comes with a pre-made *Travis CI* configuration located at ``.travis.yml``.

.. important::

   You need to `host the project in Github <#github>`__ to use Travis CI. 

Please follow the `official Travis CI documentation <https://docs.travis-ci.com/user/tutorial/>`_ for instructions to grant *Travis CI* access to the repository.

Once enabled, Travis CI runs `all of the tests mentioned above <#testing>`__ automatically after each push. You can view the results at:

``https://travis-ci.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}``

Travis CI also generates code coverage reports for the starter Python package, which can be viewed at *codecov*: 

``https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}``

.. note::

   Please refer to the `official guide <https://docs.codecov.io/docs>`__ to how to quick-start and use *codecov*.

Online Documentation
=========================================

You may want to host the `Sphinx documentation <#documentation>`__ online, e.g. at `Read the Docs <https://readthedocs.io>`__ or `Github Pages <https://pages.github.com/>`__. Typically, these services offer effortless integration with *Github*. Please refer to these services to learn how.

.. note::

   We assume that you will host the documentation at ``https://{{ cookiecutter.repo_slug}}.readthedocs.io``. Please modify the URLs in the project ``README`` and documentation, if you would like to host it elsewhere.
