# Kerning Recursive Sans

## General process

1. Copy "normal-width," 600-unit glyphs from Mono to Sans
2. Adjust non-normal-width glyphs for Sans, ensuring glyph widths are constant between a Sans masters
3. Kern in one Sans master (probably, Casual B, because it is a generally basic weight and more likely to crash than the Linear styles, due to its curved diagonal forms)
4. Copy this kerning to other Sans masters, to ensure that width metrics remain constant across Sans masters


## Challenges

### Copying kerning efficiently

I will continue to improve this flow, but for now, I am using a beta version of Metrics Machine, which includes an early-release API. This is very helpful in allowing me to easily copy kerning from one master to many others.

[Here is the script as of Oct 20, 2019](https://github.com/arrowtype/recursive/blob/6bbafc1351e665ff37219fc3c9d2d0b2d956a6dd/src/00-recursive-scripts-for-robofont/kerning/import-MM_kerning-from_selected_font.py), but I will be improving this.
- hard-coding the source paths, to make it a one-click script
- maybe adding a separate script to display test strings for other masters

### Some glyphs could get better kerning with shape adjustments ... but they are 600-unit glyphs

- /a should be copied over from Mono, but will probably kern better with a bit less of a prominent hook (or at least, a more consistent amount of slope to the left side, across masters)
- /v is somewhat too narrow within its space, and so it doesn't space quite as well as other glyphs

Question: should glyphs like this be adjusted in Mono, before being brought over? If so, I should perhaps refactor this copier script (or make a simplified version?) to make this process faster.

- [ ] decide how to edit 600-unit glyphs for better spacing