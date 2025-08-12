#!/bin/bash
PYTHONPATH="$PYTHONPATH;.."

rm -rf docs
mkdir docs

# Outputs lot of errors, but DOES generate docs:
pdoc ./cornsnake !cornsnake.setup --output-directory  docs

echo "Outputs lot of errors, but DOES generate docs"
echo "./docs"
ls -al docs
