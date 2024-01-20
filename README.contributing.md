# cornsnake - contributing

## Dev dependencies

- pyenv - if on Windows use [pyenv-win](https://github.com/pyenv-win/pyenv-win) [needs an Adminstrator Powershell terminal]

## Install

Switch to Python 3.11.6:

```
pyenv install 3.11.6
pyenv local 3.11.6
```

Setup a virtual environment:

```
./create_env.sh
```

If you are contributing to this project, then you need to install these extra dev dependencies:

```
pip install build parameterized twine

python -m pip install pip-tools bumpver
```

- bumpver for release versioning
- parameterized for unit tests
- build and twine are for publishing to pypi
- pip-tools is for compiling requirements.txt

## Unit Tests

```
./test.sh
```

OR:

```
./test.unit.one.sh <name of test file>
```

## Publishing

1. [OPTIONAL][if dependencies have changed] update dependencies (requirements.txt)

```
pip-compile pyproject.toml --strip-extras
```

2. deploy

```
./build-and-deploy.sh
```

## e2e Tests (after publishing)

./test.e2e.sh

## References

- https://realpython.com/pypi-publish-python-package/
