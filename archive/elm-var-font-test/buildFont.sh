#!/usr/bin/env sh

folder=RomanMasters
font=elm-mono

# build the OTF version -- this requires the AFDKO toolkit
# which is available at https://github.com/adobe-type-tools/afdko
buildmasterotfs $folder/$font.designspace
buildcff2vf $folder/$font.designspace