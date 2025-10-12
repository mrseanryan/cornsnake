#!/bin/bash
#
# example: ./test.unit.one.sh  tests.unit.test_util_list
set -e

python -m unittest $1
