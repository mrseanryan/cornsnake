#!/bin/bash
# so future errors halt the script.
set -e

./format.sh

echo Linting ...

python -m ruff check cornsnake

python -m mypy --install-types --non-interactive cornsnake

echo [done]
