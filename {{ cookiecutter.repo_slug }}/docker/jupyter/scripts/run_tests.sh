#!/bin/bash
set -e

./wait-for-it.sh $1:$2 -t $3 -- \
    echo "Running pytest as $USER with uid $UID" && \
    pytest -vv "$(pwd)/docker"

echo "Testing if {{ cookiecutter.package_name.replace('_', '-') }} is installed in editable mode"
ls /opt/conda/lib/python3.7/site-packages/{{ cookiecutter.package_name.replace('_', '-') }}.egg-link
