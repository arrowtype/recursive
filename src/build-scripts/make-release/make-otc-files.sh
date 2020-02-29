# run on Static_OTF folder, e.g.
# src/build-scripts/make-release/make-otc-files.sh

set -e
source venv/bin/activate

# use dir as argument
dir=$1

if [[ -z $dir || $dir = "--help" ]] ; then
    echo 'Add a dir path, such as:'
    echo 'src/build-scripts/make-release/make-otc-files.sh fonts/recursive_beta_1.040/Static_TTF'
    exit 2
fi

fonts=$(ls $dir/*.*tf)

otf2otc $fonts -o "$dir/recursive-statics.otc"
