#!/bin/sh


# This is a super simple shell script to speed up a test proces I was doing by hand
# 
# USAGE
# 1. Start by making some "Preview" UFOs from RoboFont Skateboard
# 2. Edit the variables below, as needed, then run the script:
#    chmod +x <path>/build-previews.sh
#    <path>/build-previews.sh <three-digit version number>

# ----------------------------------------------------------------------------------------------
# EDIT THESE VARIABLES AS NEEDED

oldFamilyName="recursive-mono-casual-a_b"
oldRomanStyleName="slant_0.00_weight_450.00"
oldItalicStyleName="slant_9.45_weight_450.00"

ufoRoman="src/masters--cubic_overlapped/experimental/curvier-casual/Previews/Preview_recursive-mono-casual-a_b-slant_0.00_weight_450.00.ufo"

ufoItalic="src/masters--cubic_overlapped/experimental/curvier-casual/Previews/Preview_recursive-mono-casual-a_b-slant_9.45_weight_450.00.ufo"


# ----------------------------------------------------------------------------------------------
# shell script setup
set -e
version=$1
rm -rf master_ttf

ufoDir="src/masters--cubic_overlapped/experimental/curvier-casual/Previews"
ttfDir="master_ttf"

ttfItalic=${ufoItalic/$ufoDir/$ttfDir}
ttfItalic=${ttfItalic/"ufo"/"ttf"}

ttfRoman=${ufoRoman/$ufoDir/$ttfDir}
ttfRoman=${ttfRoman/"ufo"/"ttf"}


# ----------------------------------------------------------------------------------------------
# generate static TTF fonts 

fontmake -o ttf -u $ufoRoman

fontmake -o ttf -u $ufoItalic

# ----------------------------------------------------------------------------------------------
# freeze ss01 into italic font to activate true-italic characters by default

python src/scripts/pyftfeatfreeze.py -f 'ss01' $ttfItalic

featFreeze=${ttfItalic/".ttf"/".ttf.featfreeze.otf"}

echo $featFreeze

mv $featFreeze $ttfItalic

# ----------------------------------------------------------------------------------------------
# update name tables to have desired naming

ttx -t name $ttfRoman
ttx -t name $ttfItalic

newFamilyName=IterativeBetaV${version}

sed  -i "" -e "s/${oldFamilyName}/${newFamilyName}/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/${oldRomanStyleName}/Regular/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/-${oldRomanStyleName}/-Regular/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/ ${oldRomanStyleName}/ Regular/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/${newFamilyName} Regular/${newFamilyName}/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/0.000/0.${version}/g" ${ttfRoman/".ttf"/".ttx"} 

sed  -i "" -e "s/${oldFamilyName}/${newFamilyName}/g" ${ttfItalic/".ttf"/".ttx"} 
sed  -i "" -e "s/${oldItalicStyleName}/Italic/g" ${ttfItalic/".ttf"/".ttx"} 
sed  -i "" -e "s/-${oldItalicStyleName}/-Italic/g" ${ttfItalic/".ttf"/".ttx"} 
sed  -i "" -e "s/ ${oldItalicStyleName}/ Italic/g" ${ttfItalic/".ttf"/".ttx"} 
sed  -i "" -e "s/${newFamilyName} Italic/${newFamilyName}/g" ${ttfRoman/".ttf"/".ttx"} 
sed  -i "" -e "s/0.000/0.${version}/g" ${ttfItalic/".ttf"/".ttx"} 

# ----------------------------------------------------------------------------------------------
# merge edits back into TTFs

ttx -m $ttfRoman ${ttfRoman/".ttf"/".ttx"} 
ttx -m $ttfItalic ${ttfItalic/".ttf"/".ttx"} 

# ----------------------------------------------------------------------------------------------
# Get rid of temp files

for ttx in master_ttf/*.ttx; do
    rm $ttx
done

mv ${ttfRoman/".ttf"/"#1.ttf"} $ttfRoman
mv ${ttfItalic/".ttf"/"#1.ttf"} $ttfItalic

# ----------------------------------------------------------------------------------------------
# copy to system fonts folder

cp $ttfRoman /Users/stephennixon/Library/Fonts/${ttfRoman/"master_ttf/"/""}
cp $ttfItalic /Users/stephennixon/Library/Fonts/${ttfItalic/"master_ttf/"/""}