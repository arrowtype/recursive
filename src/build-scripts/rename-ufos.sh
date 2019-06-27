#!/bin/sh

# Note: spaces must be escaped in git mv, eg:
# git mv "$file" "${file/'Italic\ -\ gradually\ fixed'/'Slanted'}"

find src/* -name '*Strict*' -exec sh -c '
    for file do
        echo $file
        git mv "$file" "${file/'Strict'/'Linear'}"
    done
' sh {} +
