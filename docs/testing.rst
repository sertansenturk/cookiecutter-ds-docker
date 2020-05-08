Testing
==================================================

You can test the cookiecutter, the baked services, and the Python package (e.g., build, unittest, code style, linting) locally by:

.. code:: bash

    make test

This repo also has Travis CI integration enabled (`link <https://travis-ci.com/github/sertansenturk/cookiecutter-ds-docker>`_). This service automatically runs all of the checks mentioned above after each push. Travis CI also generates code coverage reports for the Python package, which you can view on codecov (`link <https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker/>`_).
