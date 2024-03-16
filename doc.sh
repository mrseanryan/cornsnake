PYTHONPATH="$PYTHONPATH;.."

rm -rf docs
mkdir docs

# Outputs lot of errors, but DOES generate docs:
pdoc cornsnake_src !cornsnake_src.setup --output-directory  docs

ls -al docs
