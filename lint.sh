# so future errors halt the script.
set -e

echo Linting ...

ruff check cornsnake

python -m mypy --install-types --non-interactive cornsnake

echo [done]
