set -e

./test.sh

python -m build
twine check dist/*
