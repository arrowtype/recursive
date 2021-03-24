# !/bin/bash

# A script to normalize UFOs in a directory.

set -e
source venv/bin/activate

# use designspace as argument
dir=$1

if [[ -z $dir || $dir = "--help" ]] ; then
    echo 'Add a directory of UFOs, like:'
    echo 'src/01-shell-scripts-for-sources/normalize-UFOs-in-dir.sh src/ufo/sans'
    exit 2
fi

for ufo in $dir/*.ufo; do
    echo "normalizing: $ufo"
    ufonormalizer "$ufo"
done

