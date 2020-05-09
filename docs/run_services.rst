Running the Services
====================

.. Note::

   Project functionality: XX

The common commands to interact with the project are wrapped in a ``Makefile``. Below, we explain these operations. For all options, please refer to the help by running on the terminal:

.. code:: bash

    cd /{ base_folder }/{{ cookiecutter.repo_slug }}
    make help

Running the Docker Stack
------------------------

To build and run the Docker stack in a cut project, simply run:

.. code:: bash

    make

For convenience, the above command stops running stacks (if exist), cleans, (re)builds, and starts the services. It also installs a Python package called ``{{ cookiecutter.package_name }}``, which is located at ``./src/`` to the Jupyter docker service. The package is "pip installed"  in **editable** mode and the **project's base folder is mounted** on the Jupyter docker container so that all modifications are synchronized.

Accessing Jupyter UI
^^^^^^^^^^^^^^^^^^^^

Once the stack is up and running, you will see a link on the terminal, e.g., http://127.0.0.1:8888/?token=3c321..., which you can follow to access the *JupyterLab* interface from your browser. 

Accessing mlflow UI
^^^^^^^^^^^^^^^^^^^

You can reach the *mlflow* UI at http://localhost:5000. For a simple example on how to track a run, please refer to `{{ cookiecutter.package_name }}/notebooks/mlflow\_example.ipynb <https://github.com/sertansenturk/cookiecutter-ds-docker/blob/master/%7B%7B%20cookiecutter.repo_slug%20%7D%7D/notebooks/mlflow_example.ipynb>`__.

For thorough tutorials, please refer to the `official mlflow documentation <https://mlflow.org/docs/latest/tutorials-and-examples/index.html>`__.

Additional Run Options
----------------------

By default, we base the Jupyter service on the official `scipy-notebook <https://hub.docker.com/r/jupyter/scipy-notebook/tags>`__ image. You can also build & run from `tensorflow <https://hub.docker.com/r/jupyter/tensorflow-notebook/tags>`__ or `pyspark <https://hub.docker.com/r/jupyter/pyspark-notebook/tags>`__ notebooks by:

.. code:: bash

    make tensorflow
    make pyspark

If you want to use classic Jupyter notebooks, run instead:

.. code:: bash

    make notebook
