*****************************************
Setup
*****************************************

If you want to build the stack from the cut project without starting it, run:

.. code:: bash

   make build

The above command will build these images:

======================= ====================================================================================
 Service                 Image name                                                                         
======================= ====================================================================================
 *jupyter*               ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/jupyter:0.1.0``  
 *mlflow*                ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/mlflow:0.1.0``   
 *postgres*              ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/postgres:0.1.0`` 
======================= ====================================================================================

.. note::

   The version tag of docker images is read from the ``VERSION`` variable in ``.env`` file.

If you need to make a clean start:

.. code:: bash

   make clean-all
