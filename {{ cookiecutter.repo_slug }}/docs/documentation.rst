
*****************************************
Documentation
*****************************************

The project comes with a basic documentation, which is located at ``{{ cookiecutter.repo_slug }}/docs``. You can use `Sphinx <https://www.sphinx-doc.org>`__ to build the documentation locally:

.. code:: bash

   make sphinx-html

The above command builds a docker image called ``{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/sphinx`` and starts a container from the image, which -in turn- builds the documentation. Then, you can then access the documentation by opening ``{{ cookiecutter.repo_slug }}/docs/_build/html/index.html`` on your browser.
