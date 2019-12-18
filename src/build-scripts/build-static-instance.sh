# Builds a specific interpolated instance, rather than all instances (as the build-statics.sh script does)
# Helpful for faster testing of names, etc.
# add and argument with the instance you want, if not Linear Regular (like "Recursive Mono-Linear Italic.*")
# 
# NOTE: the designspace instances *must* include 'name' attributes for this to work

set -e

source venv/bin/activate

DS=$1

finalDirectory="font_betas/test_builds"
mkdir -p $finalDirectory

if [[ $2 ]] ; then
    fontmake -m $DS -o ttf -i "$2" --output-dir $finalDirectory --expand-features-to-instances
else
    
    # fontmake -m $DS -o ttf -i "Recursive Mono Linear-Regular.*" --output-dir $finalDirectory --expand-features-to-instances
    # fontmake -m $DS -o ttf -i "Recursive Mono Linear-Italic.*" --output-dir $finalDirectory --expand-features-to-instances
    fontmake -m $DS -o ttf -i "Recursive Sans Linear-Regular.*" --output-dir $finalDirectory --expand-features-to-instances
    fontmake -m $DS -o ttf -i "Recursive Sans Linear-Italic.*" --output-dir $finalDirectory --expand-features-to-instances
fi

## Set versioned names
for font in $finalDirectory/*; do
    echo $font
    python src/build-scripts/set-versioned-font-names.py "$font" --inplace
done

## get name tables
# for font in $finalDirectory/*; do
#     ttx -t name "$font"
# done