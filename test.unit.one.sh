set -e

pushd cornsnake
python -m unittest $1
popd
