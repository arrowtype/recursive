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
else
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
# fontmake -m $DS -o $fontFormat -i "Recursive Mono-Linear Regular.*" # test version
fontmake -m $DS -o $fontFormat -i

# Move
for font in "instance_${fontFormat}"/*; do
    mv "${font}" ${finalDirectory}
done

rm -r "instance_${fontFormat}"

# Set versioned names
for font in $finalDirectory/*; do
    python src/build-scripts/set-versioned-font-names.py "$font" --inplace
done

# Make woff2 files

woff2Directory="${outputDir}/static_fonts/${fontName}-static_woff2"
mkdir -p $woff2Directory

for font in $finalDirectory/*.*tf; do
    python src/build-scripts/set-up-RIBBI-style_linking.py "$font" --inplace
done

for font in $finalDirectory/*.*tf; do
    woff2_compress "$font"
done

# move woff2 files
for font in $finalDirectory/*.woff2; do
    mv "$font" $woff2Directory
done
