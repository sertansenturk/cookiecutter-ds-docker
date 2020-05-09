Setup
==================================================

Prerequisites
---------------------------------------------------

- **docker**
- **homebrew** (Optional for *Mac OSX*)
- **Python cookiecutter**

Installing docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Please follow the instructions in the `official docker documentation <https://docs.docker.com/get-docker/>`_.

(Optional) Installing homebrew in Mac OSX 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The easiest way to install *cookiecutter* in Mac OSX is using *homebrew* (see below). Please follow the instructions in the `official homebrew website <https://brew.sh/>`__ to install `homebrew`.

Installing cookiecutter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing `cookiecutter` in Ubuntu and Mac OSX is straightforward:

+--------------------+-----------------------------------+
| OS                 | Command                           |
+====================+===================================+
| *Ubuntu Linux*     | ``sudo apt install cookiecutter`` |
+--------------------+-----------------------------------+
| *Mac OSX*          | ``brew install cookiecutter``     |
+--------------------+-----------------------------------+

Please refer to the `official cookiecutter documentation <https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter>`__ for other options.

Cutting a New Project
---------------------------------------------------

To "cut" a new project from the template, run:

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

Building the Docker Stack
-------------------------

.. Note::

   Project functionality: XX

If you want to build the stack from the cut project without starting it, run:

.. code:: bash

    cd /{ base_folder }/{{ cookiecutter.repo_slug }}
    make build

If you need to make a clean start:

.. code:: bash

    make clean-all
    make build
