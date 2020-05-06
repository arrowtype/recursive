# run on fonts build folder, e.g.
# src/build-scripts/make-release/00-prep-release.sh fonts_1.042


# ---------------------------------------------
# CONFIGURATION

desktopDir="Recursive_Desktop"
desktopCodeDir="Recursive_Code"
webDir="Recursive_Web"

# ---------------------------------------------
# Script setup

set -e
source venv/bin/activate

# required argument: directory with built fonts
dir=$1
version=$(cat version.txt) # too clever
# version=${dir/"fonts_"/""}

if [[ -z $dir || $dir = "--help" ]] ; then
    echo 'Add a dir path, such as:'
    echo 'src/build-scripts/make-release/00-prep-release.sh fonts_1.042'
    exit 2
fi

# make folder name for outputs
outputDir=Recursive-${version/" "/"_"}
# clean up past runs
# rm -rf $outputDir
# rm -rf fonts/$outputDir
# rm -rf fonts/$outputDir.zip

# make folders for outputs
mkdir -p $outputDir
mkdir -p $outputDir/$desktopDir
mkdir -p $outputDir/$desktopCodeDir
mkdir -p $outputDir/$webDir

# ---------------------------------------------
# copy variable TTF

VF=$dir/Variable_TTF/*.ttf
cp $VF $outputDir/$desktopDir/$(basename $VF)

# ---------------------------------------------
# make variable woff2

woff2_compress $VF
fontFile=$(basename $VF)
woff2file=${fontFile/.ttf/.woff2}
mkdir -p "$outputDir/$webDir/woff2_variable"
mv $dir/Variable_TTF/$woff2file $outputDir/$webDir/woff2_variable/$woff2file

# ---------------------------------------------
# make web subsets

# make temp copy of VF ttf
webVFttf=$outputDir/$webDir/$(basename $VF)
cp $VF $webVFttf

# make subsets with separate shell script
src/build-scripts/make-release/unicode_range-subsets.sh $webVFttf

# remove temp variable ttf
rm $webVFttf

# ---------------------------------------------
# make TTFs in woff2

ttfFonts=$(ls $dir/Static_TTF/*.ttf)
mkdir -p $outputDir/$webDir/woff2_static

for font in $ttfFonts; do
	woff2_compress $font
	fontFile=$(basename $font)
	woff2file=${fontFile/.ttf/.woff2}
	mv $dir/Static_TTF/$woff2file $outputDir/$webDir/woff2_static/$woff2file
done

# ---------------------------------------------
# make otc & ttc collections

fonts=$(ls $dir/Static_OTF/*.otf)
otf2otc $fonts -o "$outputDir/$desktopDir/recursive-statics.otc"

fonts=$(ls $dir/Static_TTF/*.ttf)
otf2otc $fonts -o "$outputDir/$desktopDir/recursive-statics.ttc"

# ---------------------------------------------
# Make code-specific fonts

python src/build-scripts/make-release/instantiate-code-fonts.py $dir/Variable_TTF/*.ttf -o $outputDir/$desktopCodeDir

# ---------------------------------------------
# copy metadata

cp OFL.txt $outputDir/LICENSE.txt
cp $(dirname $0)/data/release-notes--all.md $outputDir/README.md
cp $(dirname $0)/data/release-notes--code.md $outputDir/$desktopCodeDir/README.md
cp $(dirname $0)/data/release-notes--desktop.md $outputDir/$desktopDir/README.md
cp $(dirname $0)/data/release-notes--web.md $outputDir/$webDir/README.md

# ---------------------------------------------
# make a zip of the outputDir, then move both dir & zip into "fonts/"

zip $outputDir.zip -r $outputDir

mv $outputDir.zip fonts
mv $outputDir fonts
