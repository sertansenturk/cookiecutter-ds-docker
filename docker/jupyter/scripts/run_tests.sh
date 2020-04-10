#!/bin/bash
set -e

sleep 5
sudo -H \
    -u \#${NB_UID} \
    MLFLOW_TRACKING_URI=${MLFLOW_TRACKING_URI} \
    bash -c \
        'echo "Running pytest as $USER with uid $UID";
         pytest -vv "$(pwd)/docker"'
