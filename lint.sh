# so future errors halt the script.
set -e

echo Linting ...

# Disable less useful errors
# - ref https://www.flake8rules.com/
#
# E302 Expected 2 blank lines
# E305 Expected 2 blank lines after end of function or class
# E501 Line too long (82 > 79 characters)
FLAKE8_TO_IGNORE=E302,E305,E501

# Disable flake8 warning about unused import
FLAKE8_FILES_TO_IGNORE="./src\cornsnake\__init__.py:F401"

# Unix
if [ -f /usr/bin/python3.11 ]; then
  echo Using python at /usr/bin/python3.11
  /usr/bin/python3.11 -m flake8 --extend-ignore $FLAKE8_TO_IGNORE --per-file-ignores $FLAKE8_FILES_TO_IGNORE ./src
else
  # Windows
  echo Using python at python
  python -m flake8 --extend-ignore $FLAKE8_TO_IGNORE --per-file-ignores=$FLAKE8_FILES_TO_IGNORE ./src
fi

echo [done]
