#!/usr/bin/env bash

set -e

_DIR=$(dirname $(realpath "$0"))

cd $_DIR

apt install -y libgl1-mesa-glx

python -m pip install -r ./requirments.txt
