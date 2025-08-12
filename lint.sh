#!/bin/bash
# so future errors halt the script.
set -e

./format.sh

echo Linting ...

ruff check cornsnake

python -m mypy --install-types --non-interactive cornsnake

echo [done]
