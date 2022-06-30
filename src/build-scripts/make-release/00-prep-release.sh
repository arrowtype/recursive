#!/bin/bash

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
version=${dir: 6:5} # assumes the folder has a name like 'fonts_1.067' or 'fonts_1.067_ignore'

if [[ -z $dir || $dir = "--help" ]] ; then
    echo 'Add a dir path, such as:'
    echo 'src/build-scripts/make-release/00-prep-release.sh fonts_1.042'
    exit 2
fi

# make folder name for outputs
outputDir=ArrowType-Recursive-${version/" "/"_"}
gfDir=fonts/recursive_for_googlefonts

# clean up past runs
rm -rf "./$outputDir" || true           # move on if dir isn't there to delete
rm -rf fonts/$outputDir || true     # move on if dir isn't there to delete
rm -rf fonts/$outputDir.zip || true # move on if dir isn't there to delete
rm -rf $gfDir || true               # move on if dir isn't there to delete

# ---------------------------------------------
# if you need to make sure versions are set to something specific

# python src/build-scripts/make-release/change-font-versions-in-dir.py $dir $version

# ---------------------------------------------
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
src/build-scripts/make-release/make-variable-woff2s_and_subsets.sh $webVFttf

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
otf2otc $fonts -o "$outputDir/$desktopDir/recursive-static-OTFs.otc"

fonts=$(ls $dir/Static_TTF/*.ttf)
otf2otc $fonts -o "$outputDir/$desktopDir/recursive-static-TTFs.ttc"

# ---------------------------------------------
# copy metadata

cp OFL.txt $outputDir/LICENSE.txt
cp $(dirname $0)/data/release-notes--all.md $outputDir/README.md
cp $(dirname $0)/data/release-notes--code.md $outputDir/$desktopCodeDir/README.md
cp $(dirname $0)/data/release-notes--desktop.md $outputDir/$desktopDir/README.md
# cp $(dirname $0)/data/release-notes--web.md $outputDir/$webDir/README.md

# ---------------------------------------------
# copy separate statics, in case people want these

mkdir -p $outputDir/$desktopDir/separate_statics

cp -r $dir/Static_OTF $outputDir/$desktopDir/separate_statics/OTF
rm $outputDir/$desktopDir/separate_statics/OTF/*_output.txt || true # remove file if it exists OR move on

cp -r $dir/Static_TTF $outputDir/$desktopDir/separate_statics/TTF
rm $outputDir/$desktopDir/separate_statics/TTF/*_output.txt || true # remove file if it exists OR move on

# ---------------------------------------------
# move dir into "fonts/"

mv $outputDir fonts/$outputDir

# ---------------------------------------------
# Prep release for Google Fonts

mkdir -p $gfDir

cp $VF "$gfDir/Recursive[CASL,CRSV,MONO,slnt,wght].ttf"

cp -r $dir/Static_TTF $gfDir/static
rm $gfDir/static/*_output.txt || true # remove file if it exists OR move on

# ---------------------------------------------
# make code fonts
# assumes the "recursive-code-config" project lives in the same directory as "recursive"


mkdir -p fonts/$outputDir/$desktopCodeDir

# gets VF filename
VFname=$(basename $VF)
# copy VF into code-config directory
cp $VF ../recursive-code-config/font-data/$VFname

# move there
cd ../recursive-code-config

# install requirements for recursive-code-config
pip install -U -r requirements.txt

echo recursive-code-config/font-data/$VFname

# run scripts/build-all.sh $VFcopy
scripts/build-all.sh font-data/$VFname

# copy each dir in ./fonts back into ../recursive/fonts/$outputDir/Recursive_Code
fontDirs=$(ls ./fonts)

for fontDirPath in $fontDirs; do
	cp -a "fonts/$fontDirPath/." ../recursive/fonts/$outputDir/Recursive_Code/$(basename "$fontDirPath")
done

# move back
cd ../recursive

# ---------------------------------------------
# make zip of final release

cd fonts
zip $outputDir.zip -r $outputDir -x .DS_*