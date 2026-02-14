#!/bin/bash
# bumpver can fail the first time (NOT line endings)
# set -e

uv run bumpver update --patch
uv run bumpver update --patch
