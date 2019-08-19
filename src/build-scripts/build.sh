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

fontmake -m $DS -o variable --output-path $outputDir/$fontName--$date.ttf

# version the font name
python src/build-scripts/set-versioned-font-names.py $outputDir/$fontName--$date.ttf
mv $outputDir/$fontName--$date.ttf.fix $outputDir/$fontName--$date.ttf

# make woff2
woff2_compress $outputDir/$fontName--$date.ttf

# add subset base64 of woff2 for testing in CodePen, etc

pyftsubset $outputDir/$fontName--$date.ttf --unicodes="U+0020-007F" --flavor="woff2" --output-file="$outputDir/$fontName--$date--subset-0020_007F.woff2"

base64 "$outputDir/$fontName--$date--subset-0020_007F.woff2" > "$outputDir/$fontName--$date--subset-0020_007F.base64"

# rm "$outputDir/$fontName--$date--subset-0020_007F.woff2"
