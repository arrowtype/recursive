# !/bin/bash

# HOW TO USE: 
# remove-kerning-groups-ufos.sh <family dir>
#
# src/build-scripts/remove-kerning-groups-ufos.sh src/masters/sans/recursive-varfontprep-2019_08_12-01_24_58

set -e
source venv/bin/activate

echo hello

UFOs=$1

find $UFOs/* -name '*kerning.plist' -exec sh -c '
    for file do
        rm "$file"
        echo 🔥 removed "$file"
    done
' sh {} +

find $UFOs/* -name '*groups.plist' -exec sh -c '
    for file do
        rm "$file"
        echo 🔥 removed "$file"
    done
' sh {} +

