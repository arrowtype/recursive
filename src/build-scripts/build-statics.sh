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

# Sort out path naming

if [[ $2 = "-o" || $2 = "--otf" ]] ; then
    fontFormat="otf"
elif [[ $2 = "-t" || $2 = "--ttf" ]] ; then
    fontFormat="ttf"
fi

outputDir="font_betas"
dsName=$(basename $DS)
fontName=${dsName/".designspace"/""}
finalDirectory="${outputDir}/static_fonts/${fontName}-static_${fontFormat}"

echo $fontName
echo $finalDirectory

mkdir -p $finalDirectory

# Build
echo 🏗 Building static $fontFormat files
fontmake -m $DS -o $fontFormat -i

# Move
for font in "instance_${fontFormat}"/*; do
    mv "${font}" ${finalDirectory}
done

rm -r "instance_${fontFormat}"

# Set versioned names
for font in $finalDirectory/*; do
    python src/build-scripts/set-versioned-font-names.py "$font" --static --inplace
done

