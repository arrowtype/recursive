dir=$1


OIFS="$IFS"
IFS=$'\n'
for italic in `find $dir -type f -name "*Italic.otf"`  
do
    echo $italic
    #  diff "$file" "/some/other/path/$file"
    #  read line
    python src/build-scripts/pyftfeatfreeze.py -f 'ss01' $italic

    featFreeze=${italic/".otf"/".otf.featfreeze.otf"}

    mv $featFreeze $italic    
done
IFS="$OIFS"

# python src/build-scripts/pyftfeatfreeze.py -f 'ss01' $ttfItalic

# featFreeze=${ttfItalic/".ttf"/".ttf.featfreeze.otf"}

# echo $featFreeze

# mv $featFreeze $ttfItalic