# Builds a specific interpolated instance, rather than all instances (as the build-statics.sh script does)
# Helpful for faster testing of names, etc.
# add and argument with the instance you want, if not Linear Regular (like "Recursive Mono-Linear Italic.*")
# 
# NOTE: the designspace instances *must* include 'name' attributes for this to work

DS=$1

outputDir="font_betas"
dsName=$(basename $DS)
fontName=${dsName/".designspace"/""}
finalDirectory="${outputDir}/static_fonts/${fontName}-static_ttf"


if [[ $2 ]] ; then
    fontmake -m $DS -o ttf -i "$2" --output-dir $finalDirectory
else
    fontmake -m $DS -o ttf -i "Recursive Mono-Linear Regular.*" --output-dir $finalDirectory
fi

# Set versioned names
for font in $finalDirectory/*; do
    python src/build-scripts/set-versioned-font-names.py "$font" --inplace
done