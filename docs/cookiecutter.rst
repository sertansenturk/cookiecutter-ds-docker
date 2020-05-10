.. sectnum:: 

#########################################
Cookiecutter Template
#########################################

*****************************************
Setup
*****************************************

``cookiecutter-ds-docker`` requires these tools as a prerequisite:

- **docker**
- **homebrew** (Optional for *Mac OSX*)
- **Python cookiecutter**

Installing docker
=========================================

Please follow the instructions in the `official docker documentation <https://docs.docker.com/get-docker/>`_.

(Optional) Installing homebrew in Mac OSX
=========================================

*homebrew* is the easiest way to install *cookiecutter* in Mac OSX (see below). Please follow the instructions in the `official website <https://brew.sh/>`__, if you wish to install `homebrew`.

Installing cookiecutter
=========================================

*cookiecutter* is quite straightforward to install in many modern systems. For example, you can install `cookiecutter` in *Debian-based Linux* distributions (e.g., *Ubuntu*) and *Mac OSX* by:

+----------------------+-----------------------------------+
| OS                   | Command                           |
+======================+===================================+
| *Debian-based Linux* | ``sudo apt install cookiecutter`` |
+----------------------+-----------------------------------+
| *Mac OSX*            | ``brew install cookiecutter``     |
+----------------------+-----------------------------------+

Please refer to the `official cookiecutter documentation <https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter>`__ for alternatives.

*****************************************
Cutting a New Project
*****************************************

To "cut" a new project from the template, run on the terminal:

.. code:: bash

    cd /{ base_folder }
    cookiecutter https://github.com/sertansenturk/cookiecutter-ds-docker

*cookiecutter* will ask you to fill a few variables, namely:

+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Variable             | Explanation                                      | Modifies                                                                                                       |
+======================+==================================================+================================================================================================================+
| *repo\_name*         | Name of the repository                           | Header of ``README.md``                                                                                        |
+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| *repo\_slug*         | Slug of the repository name                      | Repository folder name, GitHub URL, explanations in ``README.md``                                              |
+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| *package\_name*      | Name of the Python package in the project        | Python package name, ``setup.py``, ``tox.ini``, unittests, docker image names, explanations in ``README.md``   |
+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| *author\_name*       | Name of the authoring person/team/organization   | Author name in ``setup.py`` and ``README.md``                                                                  |
+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| *author\_email*      | E-mail to contact the author                     | Author e-mail in ``setup.py``, ``CODE_OF_CONDUCT.md`` and ``README.md``                                        |
+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| *github\_username*   | Github username                                  | GitHub URL, URLs in ``setup.py``, docker image names, explanations in ``README.md``                            |
+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| *description*        | A short description of the project               | Explanations in ``setup.py`` and ``README.md``                                                                 |
+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

Afterward, the project will be created in ``/{ base_folder }/{{ cookiecutter.repo_slug }}``.

For additional command line options, please refer to the `advanced options <https://cookiecutter.readthedocs.io/en/latest/advanced/cli_options.html#command-line-options>`__ in the official cookiecutter documentation.

*****************************************
Local Usage
*****************************************

.. attention::
   You should clone the repo if you would like to use *cookiecutter-ds-docker* locally or modify the template:

   .. code:: bash

      git clone https://github.com/sertansenturk/cookiecutter-ds-docker.git
      cd cookiecutter-ds-docker

Below, we introduce some useful ``Makefile`` commands to interact with ``cookiecutter-ds-docker``. For all available commands, please refer to the help by running:

.. code:: bash

   make help

Cutting a New Project Locally
=========================================

You can cut a project by running:

.. code:: bash

    make

and entering the variables, as `explained above <#cutting-a-new-project>`__. The project will be created at ``../{{ cookiecutter.repo_slug }}`` relative to the ``./cookiecutter-ds-docker`` folder.

Documentation
=========================================

We use `Sphinx <https://www.sphinx-doc.org>`__ for documentation. The documentation is hosted online at `Read the Docs <https://cookiecutter-ds-docker.readthedocs.io>`_. *Read the Docs* automatically publishes and updates a version for the *master* branch, *dev* branch, and each release in *Github*.

If you would like to build the documentation locally, you need to run:

.. code:: bash

    make sphinx-html

Then, you can then access the documentation by opening ``./docs/_build/html/index.html`` on your browser.

To validate the documentation without building, run:

.. code:: bash

    make sphinx-html-test

Running Tests Locally
=========================================

You can run the tests with a single command by:

.. code:: bash

    make test

The above command:

1. Cuts a dummy project and runs the all tests inside (See `Project Testing Section <ds_docker_project.html#testing>`__)
2. Validates the Sphinx documentation (See `above <#documentation>`__)

*****************************************
Tests in Travis CI
*****************************************

``cookiecutter-ds-docker`` has *Travis CI* integration (`link <https://travis-ci.com/github/sertansenturk/cookiecutter-ds-docker>`__), where all of the aforementioned tests are run automatically after each push.

*Travis CI* also generates code coverage reports for the starter Python package (`see Python Tests in the Project <ds_docker_project.html#python>`__), which can be viewed on *codecov* (`link <https://codecov.io/gh/sertansenturk/cookiecutter-ds-docker/>`__).
