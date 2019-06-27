#!/bin/sh

find src/* -name '*gradually*' -exec sh -c '
    for file do
        echo $file
        git mv "$file" "${file/'Italic\ -\ gradually\ fixed'/'Slanted'}"
    done
' sh {} +
