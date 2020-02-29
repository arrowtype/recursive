


# !/bin/bash

set -e
source venv/bin/activate

fontPath=$1
fontFile=$(basename $fontPath)
outputDir="$(dirname $fontPath)/WOFF2_subsets-wght300_800"
outputDir1="$(dirname $fontPath)/WOFF2"

mkdir -p $outputDir
mkdir -p $outputDir1

echo $fontPath
echo $fontFile
echo $outputDir

# --------------------------------------
# start by subsetting wght axis

fontPath300_800=$outputDir/${fontFile/'.ttf'/'--wght300_800.ttf'}
fontFile300_800=$(basename $fontPath300_800)
fonttools varLib.instancer $fontPath wght=300:800 -o $fontPath300_800

# --------------------------------------
# agressively-split ranges
# # based on https://en.wikipedia.org/wiki/List_of_Unicode_characters

# bare minimum English subset, plus copyright & arrows (← ↑ → ↓)
englishBasicFile=${fontFile300_800/'.ttf'/--subset_range_english_basic.woff2}
englishBasicUni="U+0020-007E,U+00A9,U+2190-2193,U+2018,U+2019,U+201C,U+201D,U+2022"
pyftsubset $fontPath300_800 --flavor="woff2" --layout-features-="numr,dnom,frac" --output-file=$outputDir/$englishBasicFile --unicodes=$englishBasicUni

# unicode latin-1 letters, basic european diacritics
latin1File=${fontFile300_800/'.ttf'/--subset_range_latin_1.woff2}
latin1Uni="U+00C0-00FF"
pyftsubset $fontPath300_800 --flavor="woff2" --output-file=$outputDir/$latin1File --unicodes=$latin1Uni

# unicode latin-1 punc/symbols (except copyright), extra arrows (↔ ↕ ↖ ↗ ↘ ↙)
latin1PuncFile=${fontFile300_800/'.ttf'/--subset_range_latin_1_punc.woff2}
latin1PuncUni="U+00A0-00A8,U+00AA-00BF,U+2194-2199"
pyftsubset $fontPath300_800 --flavor="woff2" --output-file=$outputDir/$latin1PuncFile --unicodes=$latin1PuncUni

# unicode latin A extended
latinExtFile=${fontFile300_800/'.ttf'/--subset_range_latin_ext.woff2}
latinExtUni="U+0100-017F"
pyftsubset $fontPath300_800 --flavor="woff2" --output-file=$outputDir/$latinExtFile --unicodes="U+0100-017F"


# ----------------------------------------------
# static file with unicodes for just "sia"

siaLogoFile=${fontFile/'.ttf'/--subset_sia_logo.woff2}
siaLogoUni="U+0073,U+0069,U+0061"
pyftsubset $fontPath --flavor="woff2" --output-file=$outputDir/$siaLogoFile --unicodes=$siaLogoUni

fonttools varLib.instancer $outputDir/$siaLogoFile wght=1000 slnt=0 ital=0 CASL=1 MONO=0 -o $outputDir/$siaLogoFile


__CSS="
/* SPECIFICALLY for the 'sia' karamalegos logo @ sia.code – remove if you don't need :) */
@font-face {
  font-family: 'Recursive';
  font-weight: 1000;
  font-display: swap;
  src: url('fonts/$siaLogoFile') format('woff2');
  unicode-range: $siaLogoUni;
}
 /* The bare minimum English subset, plus copyright & arrows (← ↑ → ↓) & quotes (“ ” ‘ ’) & bullet (•) */
@font-face {
  font-family: 'Recursive';
  font-style: oblique -15deg 0deg;
  font-weight: 300 800;
  font-display: swap;
  src: url('fonts/$englishBasicFile') format('woff2');
  unicode-range: $englishBasicUni;
}

/* unicode latin-1 letters, basic european diacritics */
@font-face {
  font-family: 'Recursive';
  font-style: oblique -15deg 0deg;
  font-weight: 300 800;
  font-display: swap;
  src: url('fonts/$latin1File') format('woff2');
  unicode-range: $latin1Uni;
}

/* unicode latin-1, punc/symbols & arrows (↔ ↕ ↖ ↗ ↘ ↙) */
@font-face {
  font-family: 'Recursive';
  font-style: oblique -15deg 0deg;
  font-weight: 300 800;
  font-display: swap;
  src: url('fonts/$latin1PuncFile') format('woff2');
  unicode-range: $latin1PuncUni;
}

/* unicode latin A extended */
@font-face {
  font-family: 'Recursive';
  font-style: oblique -15deg 0deg;
  font-weight: 300 800;
  font-display: swap;
  src: url('fonts/$latinExtFile') format('woff2');
  unicode-range: $latinExtUni;
}
"

echo "$__CSS" > $outputDir/fonts-wght300_800.css

# clean up wght-subset font
rm $fontPath300_800