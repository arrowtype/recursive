#!/bin/sh

# This is a super simple shell script to speed up a test process I was doing by hand
# 
# USAGE
# 1. Start by making some "Preview" UFOs from RoboFont Skateboard
# 2. Edit the variables below, as needed, then run the script:
#    chmod +x <path>/build-previews.sh
#    <path>/build-previews.sh 1.<three-digit version number>

# ---------------------------------------------------------------------------
# EDIT THESE VARIABLES AS NEEDED

# The files you're building from
ufoRoman="src/masters--cubic_overlapped/experimental/curvier-casual/Previews/Preview_recursive-mono-a_b-slant_0.00_weight_450.00_expression_0.00.ufo"
ufoItalic="src/masters--cubic_overlapped/experimental/curvier-casual/Previews/Preview_recursive-mono-a_b-slant_9.45_weight_450.00_expression_0.00.ufo"

# These might be weird – get them from the font info or from the name table
oldFamilyName="recursive-mono-a_b"
oldRomanStyleName="slant_0.00_weight_450.00_expression_0.00"
oldItalicStyleName="slant_9.45_weight_450.00_expression_0.00"


# Give a new family name
newFamilyName="IterativeBetaV"

# your system fonts folder
fontsFolder="/Users/stephennixon/Library/Fonts"

# the current source dir which is holding the "Previews" folder
sourceDir="src/masters--cubic_overlapped/experimental/curvier-casual"

ufoDir="$sourceDir/Previews"

ttfDir="master_ttf"


# ---------------------------------------------------------------------------
# shell script setup
set -e
source venv/bin/activate

version=$1
rm -rf master_ttf

echo ----------------------

ttfItalic=${ufoItalic/"$ufoDir"/"$ttfDir"}
ttfItalic=${ttfItalic/"ufo"/"ttf"}

echo TTF Italic will be $ttfItalic 

ttfRoman=${ufoRoman/"$ufoDir"/"$ttfDir"}
ttfRoman=${ttfRoman/"ufo"/"ttf"}

echo TTF Roman will be $ttfRoman 

echo ----------------------

cp $sourceDir/features.fea $ufoRoman/features.fea
cp $sourceDir/features.fea $ufoItalic/features.fea

# check that version number was included in script call

if [[ -z "$version" || $version = "--help" ]] ; then
    echo 'Add three-digit version number to your script call, like:'
    echo '$ <script_path>/build-previews.sh 1.009'
    exit 2
fi

# ---------------------------------------------------------------------------
# generate static TTF fonts 

fontmake -o ttf -u $ufoRoman

fontmake -o ttf -u $ufoItalic

# # ---------------------------------------------------------------------------
# # freeze ss01 into italic font to activate true-italic characters by default

echo $ttfItalic

python src/build-scripts/pyftfeatfreeze.py -f 'ss01' $ttfItalic

featFreeze=${ttfItalic/".ttf"/".ttf.featfreeze.otf"}

echo $featFreeze

mv $featFreeze $ttfItalic

# # ---------------------------------------------------------------------------
# # update name tables to have desired naming

ttx -t name $ttfRoman
ttx -t name $ttfItalic

newFamilyNameVersioned="${newFamilyName}${version}"

sed  -i "" -e "s/${oldFamilyName}/${newFamilyNameVersioned}/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/${oldRomanStyleName}/Regular/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/-${oldRomanStyleName}/-Regular/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/ ${oldRomanStyleName}/ Regular/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/${newFamilyNameVersioned} Regular/${newFamilyNameVersioned}/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/0.000/0.${version}/g" ${ttfRoman/".ttf"/".ttx"} 

sed  -i "" -e "s/${oldFamilyName}/${newFamilyNameVersioned}/g" ${ttfItalic/".ttf"/".ttx"} 
sed  -i "" -e "s/${oldItalicStyleName}/Italic/g" ${ttfItalic/".ttf"/".ttx"} 
sed  -i "" -e "s/-${oldItalicStyleName}/-Italic/g" ${ttfItalic/".ttf"/".ttx"} 
sed  -i "" -e "s/ ${oldItalicStyleName}/ Italic/g" ${ttfItalic/".ttf"/".ttx"} 
sed  -i "" -e "s/${newFamilyNameVersioned} Italic/${newFamilyNameVersioned}/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/0.000/0.${version}/g" ${ttfItalic/".ttf"/".ttx"} 

# ---------------------------------------------------------------------------
# merge edits back into TTFs

ttx -m $ttfRoman ${ttfRoman/".ttf"/".ttx"} 
ttx -m $ttfItalic ${ttfItalic/".ttf"/".ttx"} 

# ---------------------------------------------------------------------------
# Get rid of temp files

for ttx in master_ttf/*.ttx; do
    rm $ttx
done

mv ${ttfRoman/".ttf"/"#1.ttf"} $ttfRoman
mv ${ttfItalic/".ttf"/"#1.ttf"} $ttfItalic

# ---------------------------------------------------------------------------
# copy to system fonts folder

romanName="$newFamilyNameVersioned-Roman.ttf"
italicName="$newFamilyNameVersioned-Italic.ttf"

cp $ttfRoman "$fontsFolder/$romanName"
cp $ttfItalic "$fontsFolder/$italicName"

cp $ttfRoman "fonts/recursive-betas-for-code/$romanName"
cp $ttfItalic "fonts/recursive-betas-for-code/$italicName"

echo "-----------------------------"
echo "Roman copied to $fontsFolder/$romanName"
echo "Italic copied to $fontsFolder/$italicName"