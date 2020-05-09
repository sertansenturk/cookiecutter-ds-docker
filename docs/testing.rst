Testing and Development
==================================================

Testing the cookiecutter Template
---------------------------------

You can test the cookiecutter template - as well as the tests inside the project (`see below <#testing-the-project>`__) - locally by:

.. code:: bash

    make test

In addition, ``cookiecutter-ds-docker`` has *Travis CI* integration (`link <https://travis-ci.com/github/sertansenturk/cookiecutter-ds-docker>`__), where all of these checks are run automatically after each push. 

*Travis CI* also generates code coverage reports for the starter Python package (`see below <#testing-the-python-package>`__), which can be viewed on *codecov* (`link <https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker/>`__).

Testing the Project
-------------------

.. Note::

   Project functionality: XX

Testing the Docker Stack
^^^^^^^^^^^^^^^^^^^^^^^^

You can test the integration of the services (e.g., ``mlflow`` logging from the Jupyter service) automatically by running the docker-compose stack in test mode by executing:

.. code:: bash

    make test

Testing the Python Package
^^^^^^^^^^^^^^^^^^^^^^^^^^

Build, code style, linting checks and unittests of the starter Python package at ``./src/{{ cookiecutter.package_name }}`` using ``tox`` in a docker environment. You can run ``tox`` by:

.. code:: bash

    make tox

In addition, the repo has Travis CI integration enabled. Travis CI (`link <https://travis-ci.com/github/{{%20cookiecutter.github_username%20}}/{{%20cookiecutter.repo_slug%20}}>`__) runs all of the checks mentioned above automatically after each push, and generates code coverage reports for the Python package, which can be viewed on codecov (`link <https://codecov.io/gh/{{%20cookiecutter.github_username%20}}/{{%20cookiecutter.repo_slug%20}}/>`__).
