.. sectnum:: :start: 4

Known Issues
==================================================

1. `Issue #56 <https://github.com/sertansenturk/cookiecutter-ds-docker/issues/56>`__ (**no_fix**): In Linux, if ``DATA_DIR`` (defined in the `{{ cookiecutter.repo_slug }}/.env <https://github.com/sertansenturk/cookiecutter-ds-docker/blob/dev/%7B%7B%20cookiecutter.repo_slug%20%7D%7D/.env>`__) is in a drive formatted in NTFS, you might have permission issues when mounting the folder to the docker containers. We suggest you to cut the project into a drive, which is formatted in a native Linux filesystem.
