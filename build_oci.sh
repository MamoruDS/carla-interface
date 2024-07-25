#!/usr/bin/env sh

# how to use this script:
# podman run -it --rm \
#        -w /app \
#        -v $(pwd):/app \
#        --userns keep-id \
#        -e PYTHON_BIN=python \
#        -e PYTHONPATH=/app/src \
#        python:3.10-bookworm bash -c './build_oci.sh' 

set -e

pip install --no-cache-dir \
            -r requirements-dev.lock && \
            ./build.sh
