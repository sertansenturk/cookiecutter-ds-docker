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
 *jupyter*               ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/jupyter``  
 *mlflow*                ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/mlflow``   
 *postgres*              ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/postgres`` 
======================= ====================================================================================

.. note::

   The version tag of docker images is read from the ``VERSION`` variable in the ``.env`` file.

If you need to make a clean start:

.. code:: bash

   make clean-all
