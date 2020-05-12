*****************************************
Online Services
*****************************************

.. attention::

   Once you enable these services, you can remove this page from the documentation.

Github
=========================================

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

For more information on *Github ecosystem*, please refer to the official `help <https://help.github.com/en>`__ and `guides <https://guides.github.com/>`__.

Travis CI
=========================================

*Travis CI* is a continuous integration service to build and test projects hosted in *Github*. {{ cookiecutter.repo_slug}} comes with a pre-made *Travis CI* configuration located at ``.travis.yml``.

.. important::

   You need to `host the project in Github <#github>`__ to use Travis CI. 

Please follow the `official Travis CI documentation <https://docs.travis-ci.com/user/tutorial/>`_ for instructions to grant *Travis CI* access to the repository.

Once enabled, Travis CI runs `all of the tests <test.html>`__ automatically after each push. You can view the results at ``https://travis-ci.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}``.

Travis CI also generates code coverage reports for the starter Python package, which can be viewed at codecov ``https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}``.

Online Documentation
=========================================

You may want to host the `Sphinx documentation <documentation.html>`__ online, e.g. at `Read the Docs <https://readthedocs.io>`__ or `Github Pages <https://pages.github.com/>`__. Typically, these services offer effortless integration with *Github*. Please refer to these services to learn how.

.. note::

   We assume that you will host the documentation at ``https://{{ cookiecutter.repo_slug}}.readthedocs.io``. Please modify the URLs in the project ``README`` and documentation, if you would like to host it elsewhere.
