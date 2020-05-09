Testing
==================================================

You can test the cookiecutter, the docker-compose stack, and the installed Python package (e.g., build, unittest, code style, linting) locally by:

.. code:: bash

    make test

In addition, ``cookiecutter-ds-docker`` has *Travis CI* integration (`link <https://travis-ci.com/github/sertansenturk/cookiecutter-ds-docker>`__), in which all of the checks above are run automatically after each push. 

*Travis CI* also generates code coverage reports for the Python package, which can be viewed on *codecov* (`link <https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker/>`__).
