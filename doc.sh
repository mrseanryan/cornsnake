PYTHONPATH="$PYTHONPATH;.."

rm -rf docs
mkdir docs

# Outputs lot of errors, but DOES generate docs:
pdoc ./cornsnake !cornsnake.setup --output-directory  docs

ls -al docs
