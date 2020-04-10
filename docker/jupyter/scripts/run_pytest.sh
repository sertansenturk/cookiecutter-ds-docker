#!/bin/bash
set -e

sleep 5
echo "Running pytest as $USER with uid $UID"
pytest -vv "$(pwd)/docker"
