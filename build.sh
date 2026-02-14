#!/bin/bash
set -e

if [[ `git status --porcelain` ]]; then
  # Changes
  echo "ERROR: git has uncommitted changes"
  exit 42
else
  # No changes
  echo "git status OK"
fi

[ -d "./dist" ] && rm -rf dist

./test.sh

uv run python -m build
uv run twine check dist/*

ls -al dist
