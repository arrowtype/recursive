# run on Static_TTF folder, e.g.
# src/build-scripts/make-woff2s-in-dir.sh fonts/recursive_beta_1.040/Static_TTF

set -e
source venv/bin/activate

# use designspace as argument
dir=$1

if [[ -z $dir || $dir = "--help" ]] ; then
    echo 'Add a dir path, such as:'
    echo 'src/build-scripts/make-woff2s-in-dir.sh fonts/recursive_beta_1.040/Static_TTF'
    exit 2
fi

fonts=$(ls $dir/*.*tf)

woff2dir=$(dirname $dir)/Static_woff2

mkdir -p $woff2dir

for font in $fonts; do
	woff2_compress $font
	fontFile=$(basename $font)
	woff2file=${fontFile/.*tf/.woff2}
	woff2=$dir/$woff2file
	echo $woff2
	mv $woff2 $woff2dir/$woff2file
done
