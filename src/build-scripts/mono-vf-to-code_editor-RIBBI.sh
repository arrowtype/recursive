
VFpath=$1

python src/build-scripts/vf2s.py $VFpath -x 0.5

python src/build-scripts/vf2s.py $VFpath -i 1 -s -9.0 -x 0.5 --style Italic

python src/build-scripts/vf2s.py $VFpath -x 0.5 -w 700 --style Bold

python src/build-scripts/vf2s.py $VFpath -w 700 -i 1 -s -9.0 -x 0.5 --style "Bold Italic"