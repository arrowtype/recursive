# !/bin/bash

set -e
source venv/bin/activate

# use designspace as argument
DS=$1

if [[ -z "$DS" || $DS = "--help" ]] ; then
    echo 'Add relative path to a designspace file, such as:'
    echo 'src/build-scripts/build.sh src/ufo/mono/FONTNAME.designspace'
    exit 2
fi

# TODO: switch features to variable ss0X

# ---------------------------------------------------------
# FontMake ------------------------------------------------

outputDir="font_betas"
dsName=$(basename $DS)
fontName=${dsName/".designspace"/""}

timestamp() {
  date +"%Y_%m_%d-%H_%M"
}

date=$(timestamp)

fontmake -m $DS -o variable --output-path $outputDir/$fontName--$date.ttf

# version the font name
python src/build-scripts/set-versioned-font-names.py $outputDir/$fontName--$date.ttf
mv $outputDir/$fontName--$date.ttf.fix $outputDir/$fontName--$date.ttf

# make woff2
woff2_compress $outputDir/$fontName--$date.ttf

## add subset base64 of woff2 for testing in CodePen, etc
pyftsubset $outputDir/$fontName--$date.ttf --flavor="woff2" --output-file="$outputDir/$fontName--$date--subset-GF_latin_basic.woff2" --unicodes="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"

## base64 version for CodePen, etc
# base64 "$outputDir/$fontName--$date--subset-0020_007F.woff2" > "$outputDir/$fontName--$date--subset-0020_007F.base64"

# rm "$outputDir/$fontName--$date--subset-0020_007F.woff2"
