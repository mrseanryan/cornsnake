#!/bin/bash
set -e

echo Formatting ...

uv run ruff format
