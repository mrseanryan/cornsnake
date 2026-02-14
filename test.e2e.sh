#!/bin/bash
pushd ./tests/e2e

python -m pip install PyMuPDF --quiet
python -m pip install --upgrade cornsnake --quiet

python -m test_import_all
python -m test_import_one
