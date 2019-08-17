# !/bin/bash

set -e
source venv/bin/activate

# use designspace as argument
DS=$1
fontFormat=$2

if [[ -z "$DS" || $DS = "--help" || -z "$fontFormat" ]] ; then
    echo '\tAdd relative path to a designspace file, such as:'
    echo '\tsrc/build-scripts/build.sh src/masters/mono/FONTNAME.designspace'
    echo '\n\tAdd argument -o for static OTF files or -t for static TTF files'
    exit 2
fi

outputDir="font-betas/work-in-progress"
dsName=$(basename $DS)
fontName=${dsName/".designspace"/""}

timestamp() {
  date +"%Y_%m_%d"
}

date=$(timestamp)

buildAndMove() {
    fontFormat=$1
    echo 🏗 Building static $fontFormat files

    fontmake -m $DS -o $fontFormat -i
    mv "instance_$fontFormat" "$outputDir/$fontName_$fontFormat"

    for font in $outputDir/$fontName_$fontFormat/*; do
        python src/build-scripts/set-versioned-font-names.py "$font" --static --inplace
    done
}

if [[ $2 = "-o" || $2 = "--otf" ]] ; then
    buildAndMove "otf"
elif [[ $2 = "-t" || $2 = "--ttf" ]] ; then
    buildAndMove "ttf"
fi
