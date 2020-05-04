#!/bin/bash
set -e

./wait-for-it.sh mlflow:5000 -t 60 -- \
    echo "Running pytest as $USER with uid $UID" && \
    pytest -vv "$(pwd)/docker"
