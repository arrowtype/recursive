#!/bin/bash

# Simplifies the process of calling mastering scripts

set -e
source venv/bin/activate

# use designspace as argument
version=$1

if [[ -z $version || $version = "--help" ]] ; then
    echo 'Add a version number, such as:'
    echo 'src/build-scripts/build-vf.sh 1.038'
    exit 2
fi

cd mastering

# prep files
python build.py --varfiles -v $version

# build files
python build.py -var -v $version
