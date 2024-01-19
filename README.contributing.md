# cornsnake - contributing

## Dev dependencies

If you are contributing to this project, then you can install these extra dev dependencies:

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
pip-compile pyproject.toml
```

2. deploy

```
./build-and-deploy.sh
```

## e2e Tests (after publishing)

./test.e2e.sh

## References

- https://realpython.com/pypi-publish-python-package/
