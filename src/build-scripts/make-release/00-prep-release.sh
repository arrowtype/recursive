# Recursive-Beta_1.042
# 	recursive_desktop
# 		recursive-staticOTF_1.042.otc
# 		recursive-staticTTF_1.042.ttc
# 		recursive-variable_1.042.ttf
# 		rec_mono-for-code
# 			[rec mono as four ttc]
# 	recursive_web
# 		static_woff2
# 			[TTFs as woff2]
# 		recursive-variable_1.042.woff2
# 		subsets
# 			[figure this out]
# 
# copy OFL.txt into folder
# copy README.md (recommendations) into folder

# run on fonts folder, e.g.
# src/build-scripts/make-release/00-prep-release.sh fonts_1.042

set -e
source venv/bin/activate

# use dir as argument
dir=$1
version=$(cat version.txt)

if [[ -z $dir || $dir = "--help" ]] ; then
    echo 'Add a dir path, such as:'
    echo 'src/build-scripts/make-release/00-prep-release.sh fonts_1.042'
    exit 2
fi

# create folder for release
outputDir=Recursive-${version/" "/"_"}
mkdir -p $outputDir
echo made $outputDir


# ---------------------------------------------
# copy variable TTF

VF=$dir/Variable_TTF/*.ttf
cp $VF $outputDir/$(basename $VF)

# ---------------------------------------------
# make variable woff2

varFonts=$(ls $dir/Variable_TTF/*.ttf)

for font in $varFonts; do
	woff2_compress $font
	fontFile=$(basename $font)
	woff2file=${fontFile/.ttf/.woff2}
	mv $dir/Variable_TTF/$woff2file $outputDir/$woff2file
done

# ---------------------------------------------
# make TTFs in woff2

ttfFonts=$(ls $dir/Static_TTF/*.ttf)
mkdir -p $outputDir/static_woff2

for font in $ttfFonts; do
	woff2_compress $font
	fontFile=$(basename $font)
	woff2file=${fontFile/.ttf/.woff2}
	mv $dir/Static_TTF/$woff2file $outputDir/static_woff2/$woff2file
done

# ---------------------------------------------
# make otc & ttc collections

fonts=$(ls $dir/Static_OTF/*.otf)
otf2otc $fonts -o "$outputDir/recursive-statics.otc"

fonts=$(ls $dir/Static_TTF/*.ttf)
otf2otc $fonts -o "$outputDir/recursive-statics.ttc"

# ---------------------------------------------
# TODO: make code ttc collections






# ---------------------------------------------
# copy metadata

cp OFL.txt $outputDir/LICENSE.txt
cp $(dirname $0)/release-notes.md $outputDir/README.md

# ---------------------------------------------
# make zip of folder

zip $outputDir.zip -r $outputDir

# ---------------------------------------------
# move folder into "fonts/"

cp $outputDir fonts/$outputDir
cp $outputDir.zip fonts/$outputDir.zip
