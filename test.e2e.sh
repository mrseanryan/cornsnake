pushd tests\e2e

pip install PyMuPDF --quiet
python -m pip install --upgrade cornsnake --quiet

python -m test_import_all
python -m test_import_one
