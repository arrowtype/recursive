# !/bin/bash

set -ex
source venv/bin/activate

# use designspace as argument
DS=$1

if [[ -z "$DS" || $DS = "--help" ]] ; then
    echo 'Add relative path to a designspace file, such as:'
    echo 'src/build-scripts/build.sh src/masters/mono/FONTNAME.designspace'
    echo 'add optional argument --static or -s to build static OTF files'
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

fontmake -m $DS -o variable --output-path $outputDir/$fontName--$date.ttf

# version the font name
python src/build-scripts/set-versioned-font-names.py $outputDir/$fontName--$date.ttf

mv $outputDir/$fontName--$date.ttf.fix $outputDir/$fontName--$date.ttf

# make woff2
woff2_compress $outputDir/$fontName--$date.ttf

# add base64 of woff2 for testing in CodePen, etc
base64 $outputDir/$fontName--$date.woff2 > $outputDir/$fontName--$date.base64

# ---------------------------------------------------------
# Statics -------------------------------------------------

# if [[ $2 = "-s" || $2 = "--statics" ]] ; then
#   # mkDir = $outputDir/statics-$date
#   fontmake -m $DS -o otf -i # --output-path $outputDir/statics-$date #### fontmake: error: MutatorMath doesn't support DesignSpace sources with 'layer' attribute
# fi