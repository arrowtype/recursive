# !/bin/bash

set -ex
source venv/bin/activate

# use designspace as argument
DS=$1

if [[ -z "$DS" || $DS = "--help" ]] ; then
    echo 'Add relative path to a designspace file, such as:'
    echo 'src/build-scripts/build.sh src/masters/mono/FONTNAME.designspace'
    exit 2
fi

# ---------------------------------------------------------
# FontMake ------------------------------------------------

outputDir="font-betas/work-in-progress"
dsName=$(basename $DS)
fontName=${dsName/".designspace"/""}

timestamp() {
  date +"%Y_%m_%d"
}

date=$(timestamp)

fontmake -m $DS -o variable --output-path $outputDir/$fontName-$date.ttf

woff2_compress $outputDir/$fontName-$date.ttf

# add base64 of woff2 for testing in CodePen, etc

base64 $outputDir/$fontName-$date.woff2 > $outputDir/$fontName-$date.base64