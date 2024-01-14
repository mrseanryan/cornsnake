# cornsnake - contributing

## Dev dependencies

If you are contributing to this project, then you can install these extra dev dependencies:

```
pip install build parameterized twine

python -m pip install pip-tools
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

1. update dependencies (requirements.txt)

```
pip-compile pyproject.toml
```

2. git should have no changes

```
git status
```

3. patch

```
./bump_patch.sh
```

4. build (and test)

```
./build.sh
```

5. publish

```
./publish.sh
```
