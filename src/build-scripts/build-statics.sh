# !/bin/bash

set -ex
source venv/bin/activate

# use designspace as argument
DS=$1

outputDir="font-betas/work-in-progress"
dsName=$(basename $DS)

timestamp() {
  date +"%Y_%m_%d"
}

date=$(timestamp)


if [[ $2 = "-o" || $2 = "--otf" ]] ; then
    fontmake -m $DS -o otf -i
    mv instance_otf $outputDir/recursive-mono-static_otf

    for font in $outputDir/recursive-mono-static_otf; do
        python src/build-scripts/set-versioned-font-names.py $font --static
    done

fi

if [[ $2 = "-t" || $2 = "--ttf" ]] ; then
    fontmake -m $DS -o ttf -i
    mv instance_ttf $outputDir/recursive-mono-static_ttf
fi





# update names 

# python src/build-scripts/set-versioned-font-names.py $outputDir/$fontName--$date.ttf