set -e

pushd src/cornsnake
python -m unittest $1
popd
