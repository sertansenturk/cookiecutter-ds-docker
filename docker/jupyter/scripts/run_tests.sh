#!/bin/bash
set -e

sleep 5
id
pytest -vv "$(pwd)/docker"
