# Web usage recommendations

- `woff2_static` contains separate static fonts for 64 styles of Recursive
- `woff2_variable` contains the full Recursive variable font, plus a "Google Fonts Latin Basic" subset which covers western European languages
- `woff2_variable_subsets` contains a few useful subsets for variable fonts, along with some starter `@font-face` CSS which you can use as a starter to use these subsets in your own web projects.

## Strategies for maximizing font performance on your website

Generally, for web typography you want to use exactly as many font styles as you need to in order to deliver clear visual hierarchy and appropriate emotional impact, but not serve more data than is needed. Here are a few strategies you might consider in pursuit of that goal.

### Premade variable subsets

To usea wide range of styles on a website (all 5 variable axes of Recursive) in a way that will cover basically every character in the typical English or western-european language, you can simply use `woff2_variable/Recursive_VF_1.050--subset-GF_latin_basic.woff2`. This file is about 280kb.

However, a slightly more-nuanced strategy for performant web font usage is utilizing `unicode-range`:

> The unicode-range CSS descriptor sets the specific range of characters to be used from a font defined by @font-face and made available for use on the current page. If the page doesn't use any character in this range, the font is not downloaded; if it uses at least one, the whole font is downloaded.

— source: https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/unicode-range

The fonts in `woff2_variable_subsets` are premade woff2 subsets, accompanied by a prewritten `@font-face` CSS in `woff2_variable_subsetsfonts.css`. You can use these fonts & CSS directly in a web project, and the browser will only download fonts as needed for the characters used on a given page. For example, if a page only includes English text, it will probably only download `Recursive_VF_1.050--subset_range_english_basic.woff2`, which is 195kb for all 5 variable axes. If another page also includes a character like the Yen (¥), Copyright (©), or the NE diagonal arrow (↗), the browser will then download `Recursive_VF_1.050--subset_range_latin_1_punc.woff2`, an additional 44kb (again, with 5 variable axes).

### Static fonts & subsetting on your own

If you only need a style or two on a site, it may be practical to just use static instances. These have a fairly large character set and are each about 100kb, so you may wish to also figure out subsetting with `pyftsubset` to make these even smaller. See https://css-tricks.com/three-techniques-performant-custom-font-usage/ for an introduction to this. 

Here is a recipe you can use to make a "Google Fonts Latin Basic" subset via the command line – just be sure to replace the font filepath before running in a terminal:

```bash
pip install fonttools # you can use pip to install fonttools, which includes pyftsubset (https://pip.pypa.io/en/stable/installing/)

fontPath="PLACE/THE/FONT/FILEPATH/HERE/IN/QUOTES" # replace this with the filepath to a woff2 font

pyftsubset $fontPath --flavor="woff2" --output-file="${fontPath/'.woff2'/--subset-GF_latin_basic.woff2}" --unicodes="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
```

### Taking it further

This subsetting approach can be used directly on the full `woff2_variable/Recursive_VF_1.050.woff2` if you wish to custom-tailor the full variable font for your project.

You can even make use of the FontTools Instacner (https://github.com/fonttools/fonttools/blob/master/Lib/fontTools/varLib/instancer.py) to instanciate your own custom instances or subset variable font (e.g. keeping only the `MONO` and `wght` axes).
