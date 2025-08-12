#!/bin/bash
set -e

./lint.sh

python -m unittest discover -v tests
