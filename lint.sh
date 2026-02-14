#!/bin/bash
# so future errors halt the script.
set -e

./format.sh

echo Linting ...

uv run ruff check cornsnake

uv run mypy --install-types --non-interactive cornsnake

echo [done]
