*****************************************
Online Services
*****************************************

Github
=========================================

.. attention::

   **Setup Instructions**

   .. important::
      Once the service is enabled, remove this block.

   To host the project in *Github*, follow the steps below:

   1. Create an **empty** repository (**do not** initialize *readme*, *license*, or *.gitignore* files). See the `official Github documentation <https://help.github.com/en/github/getting-started-with-github/create-a-repo>`__ for detailed instructions.

      .. note::

         Your *Github Username* and *Repository Name* should match ``{{ cookiecutter.github_username }}`` and ``{{ cookiecutter.repo_slug }}``, respectively.

   2. Initialize git and make a first commit, e.g.:

      .. code::

         git init
         git add .
         git commit -m "First commit"

   2. Push the project to *Github*, e.g. using *https* connection:

      .. code::

         git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}.git
         git push -u origin master

``{{ cookiecutter.repo_slug }}`` is hosted at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}.

.. note::

   For more information on the *Github ecosystem*, please refer to the `official guides <https://guides.github.com/>`__.

Travis CI
=========================================

.. attention::

   **Setup Instructions**

   .. important::
      Once the service is enabled, remove this block.

   .. important::

      You need to `host the project in Github <#github>`__ to use *Travis CI*.

   Please follow the `official Travis CI documentation <https://docs.travis-ci.com/user/tutorial/>`_ for instructions to grant *Travis CI* access to the repository.

``{{ cookiecutter.repo_slug}}`` comes with *Travis CI*, a continuous integration service to build and test projects hosted in *Github*. The configuration is located at ``.travis.yml``.

*Travis CI* runs `all of the tests <test.html>`__ automatically after each push. You can view the results at https://travis-ci.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}.

.. note::

   Please refer to the `official user documentation <https://docs.travis-ci.com/>`__ to how to work with *Travis CI*.

*Travis CI* also generates code coverage reports for the `Python package <01_overview.html/#python>`__, which can be viewed at *codecov* https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}.

.. note::

   Please refer to the `official guide <https://docs.codecov.io/docs>`__ to how to use *codecov*.

Online Documentation
=========================================

You can reach the up-to-date documentation online at https://{{ cookiecutter.repo_slug}}.readthedocs.io.

.. attention::

   **Setup Instructions**

   .. important::
      Once the service is enabled, remove this block.

   You may want to host the `Sphinx documentation <documentation.html>`__ online, e.g. at `Read the Docs <https://readthedocs.io>`__ or `Github Pages <https://pages.github.com/>`__. Typically, these services offer effortless integration with *Github*. Please refer to these services to learn how.

   .. note::

      We assume that you will host the documentation at ``https://{{ cookiecutter.repo_slug}}.readthedocs.io``. Please modify the URLs in the project ``README`` and documentation, if you would like to host it elsewhere.
