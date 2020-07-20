# !/bin/bash

# HOW TO USE: 
# remove-kerning-groups-ufos.sh <family dir>
#
# src/build-scripts/remove-kerning-groups-ufos.sh src/ufo/sans/recursive-varfontprep-2019_08_12-01_24_58

set -e
source venv/bin/activate

echo hello

UFOsDir=$1

find $UFOsDir/* -name '*kerning.plist' -exec sh -c '
    for file do
        rm "$file"
        echo 🔥 removed "$file"
    done
' sh {} +

find $UFOsDir/* -name '*groups.plist' -exec sh -c '
    for file do
        rm "$file"
        echo 🔥 removed "$file"
    done
' sh {} +

