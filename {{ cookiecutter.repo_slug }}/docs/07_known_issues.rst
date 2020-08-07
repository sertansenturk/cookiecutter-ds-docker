Known Issues
==================================================

- `Issue #56 <https://github.com/sertansenturk/cookiecutter-ds-docker/issues/56>`__ (**no_fix**): In Linux, if ``DATA_DIR`` (defined in the `.env <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_slug }}/.env>`__) is in a drive formatted in NTFS, you might have permission issues when mounting the folder to the docker containers. We suggest you to cut the project into a drive, which is formatted in a native Linux filesystem.
