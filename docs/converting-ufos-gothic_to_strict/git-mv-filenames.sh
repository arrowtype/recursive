#!/bin/sh

# I have many UFO files which contain the style 
# name "Gothic," which I have decided to change to "Strict."
# This script will use `git mv` to update the style 
# names as needed, without breaking repo history.

set -ex

find src/* -name '*Gothic*' -exec sh -c '
  for file do
    git mv "$file" "${file/'Gothic'/'Strict'}"
  done
' sh {} +
