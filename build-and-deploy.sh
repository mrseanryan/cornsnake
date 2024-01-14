# git should have no changes
if [[ `git status --porcelain` ]]; then
  # Changes
  echo "ERROR: git has uncommitted changes"
  exit 42
else
  # No changes
  echo "git status OK"
fi

# patch

./bump_patch.sh

set -e # only AFTER bump, which can fail

git diff

git add . && git commit -m "Bump patch"

# build (and test)

./build.sh
./publish.sh

git status
