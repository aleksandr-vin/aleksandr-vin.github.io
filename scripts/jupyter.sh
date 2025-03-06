#!/usr/bin/env bash

#
# See https://docs.docker.com/guides/jupyter/
#
# and https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html
#

set -xe

docker run --rm -p 8889:8888 -v "$(pwd):/home/jovyan/work" quay.io/jupyter/pytorch-notebook start-notebook.py --NotebookApp.token='hello+there'
