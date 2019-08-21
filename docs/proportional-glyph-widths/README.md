# Proportional glyph widths

On the Recursive minisite, we want to display the width metrics of glyphs in the Sans styles.

To do this, I've made a script which uses FontTools to find and report the widths of glyphs in a font, saving a JSON file of the data: `src/build-scripts/get-glyph-widths-from-built-font.py`.

This JSON can then be called to with JavaScript, using `String.CodePointAt()` to determine the unicode of a particular character.

Open test/index.html in a browser to see my test, or go to https://codepen.io/thundernixon/pen/GRKNgOd
