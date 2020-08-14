# !/bin/bash

set -e
source venv/bin/activate

# use variable font filepath as argument
fontPath=$1
fontFile=$(basename $fontPath)
# fontName=${$fontFile/".ttf"/""}
outputDir="$(dirname $fontPath)/woff2_variable_subsets"
outputDir1="$(dirname $fontPath)/woff2_variable"

mkdir -p $outputDir
mkdir -p $outputDir1

echo $fontPath
echo $fontFile
echo $outputDir

# --------------------------------------------
# basic variable fonts

# full font
woff2_compress $fontPath
mv ${fontPath/'.ttf'/'.woff2'} $outputDir1/${fontFile/'.ttf'/'.woff2'}

# google fonts latin basic
pyftsubset $fontPath --flavor="woff2" --output-file="$outputDir1/${fontFile/'.ttf'/--subset-GF_latin_basic.woff2}" --unicodes="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"


# agressively-split ranges
# # based on https://en.wikipedia.org/wiki/List_of_Unicode_characters

## bare minimum English subset, plus copyright & arrows (← ↑ → ↓) & quotes (“ ” ‘ ’) & bullet (•)
englishBasicFile=${fontFile/'.ttf'/--subset_range_english_basic.woff2}
englishBasicUni="U+0020-007F,U+00A9,U+2190-2193,U+2018,U+2019,U+201C,U+201D,U+2022"
pyftsubset $fontPath --flavor="woff2" --output-file=$outputDir/$englishBasicFile --layout-features-="numr,dnom,frac" --unicodes=$englishBasicUni

# unicode latin-1 letters, basic european diacritics
latin1File=${fontFile/'.ttf'/--subset_range_latin_1.woff2}
latin1Uni="U+00C0-00FF"
pyftsubset $fontPath --flavor="woff2" --output-file=$outputDir/$latin1File --unicodes=$latin1Uni

# unicode latin-1, punc/symbols & arrows (↔ ↕ ↖ ↗ ↘ ↙)
latin1PuncFile=${fontFile/'.ttf'/--subset_range_latin_1_punc.woff2}
latin1PuncUni="U+00A0-00BF,U+2194-2199"
pyftsubset $fontPath --flavor="woff2" --output-file=$outputDir/$latin1PuncFile --unicodes=$latin1PuncUni

# unicode latin A extended
latinExtFile=${fontFile/'.ttf'/--subset_range_latin_ext.woff2}
latinExtUni="U+0100-017F"
pyftsubset $fontPath --flavor="woff2" --output-file=$outputDir/$latinExtFile --unicodes="U+0100-017F"


__CSS="
 /* The bare minimum English subset, plus copyright & arrows (← ↑ → ↓) & quotes (“ ” ‘ ’) & bullet (•) */
@font-face {
  font-family: 'Recursive';
  font-style: oblique 0deg 15deg;
  font-weight: 300 1000;
  font-display: swap;
  src: url('/fonts/$englishBasicFile') format('woff2');
  unicode-range: $englishBasicUni;
}

/* unicode latin-1 letters, basic european diacritics */
@font-face {
  font-family: 'Recursive';
  font-style: oblique 0deg 15deg;
  font-weight: 300 1000;
  font-display: swap;
  src: url('/fonts/$latin1File') format('woff2');
  unicode-range: $latin1Uni;
}

/* unicode latin-1, punc/symbols & arrows (↔ ↕ ↖ ↗ ↘ ↙) */
@font-face {
  font-family: 'Recursive';
  font-style: oblique 0deg 15deg;
  font-weight: 300 1000;
  font-display: swap;
  src: url('/fonts/$latin1PuncFile') format('woff2');
  unicode-range: $latin1PuncUni;
}

/* unicode latin A extended */
@font-face {
  font-family: 'Recursive';
  font-style: oblique 0deg 15deg;
  font-weight: 300 1000;
  font-display: swap;
  src: url('/fonts/$latinExtFile') format('woff2');
  unicode-range: $latinExtUni;
}
"

echo "$__CSS" > $outputDir/fonts.css




