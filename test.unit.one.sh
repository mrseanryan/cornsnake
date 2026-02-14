#!/bin/bash
#
# example: ./test.unit.one.sh  tests.unit.test_util_list
set -e

uv run python -m unittest $1
