Setup
==================================================

First, you have to install ``cookiecutter``. For example, you can install cookiecutter in Ubuntu or Mac by:

+--------------------+---------------------------------+
| OS                 | Command                         |
+====================+=================================+
| *Ubuntu Linux*     | ``apt install cookiecutter``    |
+--------------------+---------------------------------+
| *Mac OSX*          | ``brew install cookiecutter``   |
+--------------------+---------------------------------+

For other methods to install ``cookiecutter``, please refer to the `official documentation <https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter>`_.

Then, "baking" the template is straightforward:

.. code:: bash

    cd /[base_folder]
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
| *author\_name*       | Name of the authoring person/team/organization   | author name in ``setup.py`` and ``README.md``                                                                  |
+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| *author\_email*      | E-mail to contact the author                     | author e-mail in ``setup.py``, ``CODE_OF_CONDUCT.md`` and ``README.md``                                        |
+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| *github\_username*   | Github username                                  | GitHub URL, URLs in ``setup.py``, docker image names, explanations in ``README.md``                            |
+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| *description*        | A short description of the project               | explanations in ``setup.py`` and ``README.md``                                                                 |
+----------------------+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

Afterward, the project will be created in ``/[base_folder]/[repo_slug]``.

For additional command line options and information about Python cookiecutter, please refer to `official cookiecutter documentation <https://cookiecutter.readthedocs.io/en/latest/advanced/cli_options.html#command-line-options>`_.
