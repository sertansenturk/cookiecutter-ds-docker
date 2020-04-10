#!/bin/bash
set -e

sleep 5
sudo -H -u \#${NB_UID} bash -c 'echo "Running pytest as $USER with uid $UID"' 
sudo -H -u \#${NB_UID} bash -c 'pytest -vv "$(pwd)/docker"'
