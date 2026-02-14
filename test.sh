#!/bin/bash
set -e

./lint.sh

uv run python -m unittest discover -v tests
