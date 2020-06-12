#!/bin/bash
set -e

./wait-for-it.sh $1:$2 -t $3 -- \
    echo "Running pytest as $USER with uid $UID" && \
    pytest -vv "$(pwd)/docker"

# test if the package is installed in editable mode
# i.e. if the {{ cookiecutter.repo_slug}}.egg-link is in site-packages
ls /opt/conda/lib/python3.7/site-packages/mre.egg-linkd