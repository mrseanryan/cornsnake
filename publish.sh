set -e

./test.sh

twine check dist/*

# twine upload -r testpypi dist/*
twine upload dist/*

echo To install the package:
echo python -m pip install cornsnake
