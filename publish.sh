#!/bin/bash
set -e

./test.sh

uv run twine check dist/*

# twine upload -r testpypi dist/*
uv run twine upload dist/*

echo To install the package:
echo python -m pip install cornsnake
