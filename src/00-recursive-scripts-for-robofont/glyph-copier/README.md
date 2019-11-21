# Glyph Copier

![](assets/2019-11-21-13-10-07.png)

## Usage

This script is mainly meant for use in Recursive, to copy glyphs from Mono to Sans or (occassionally) Sans to Mono.

To use it:

0. Make a git commit to backup your current work. No guarantees that this script will do exactly what you expect it to!
1. Select glyphs you'd like to copy, then copy their names to your clipboard with *`option`+`command`+`c`*
2. Run the script in RoboFont
3. Paste in the glyph names you wish to copy
4. Select your options: 
   1. `Overwrite 600w Glyphs` will replace glyphs in the destination font if they are 600 units wide
   2. `Overwrite non-600w Glyphs` will overwrite glyphs in the destination font if they are *not* 600 units wide
   3. Trying to copy glyphs that already exist and are not included in an "overwrite" option will create them in the destination font with the suffix `.copy` added
   4. If you want, you can change the mark color for copied glyphs. The default is orange.
5. Click `Mono → Sans` to copy glyphs from Mono to Sans masters. Alternatively, `Sans → Mono` will copy from Sans to Mono masters. 
6. A file-selection dialogue will open. 
   1. Select *all* the UFOs you with to copy *from* and *to*. For example, to copy listed glyphs from `Recursive Mono–Casual B.ufo` to `Recursive Sans–Casual B.ufo`, you should select both of these in the same window. To copy glyphs from all mono to all sans masters (or vice versa), you can select all 24 masters at once.
   2. Copying is based on the style names. So, `Casual B` copies into `Casual B`. Therefore, this script will not copy glyphs between two Mono fonts, or between fonts with different style names. This makes it possible for the script to understand which UFOs are "paired" and copy between multiple pairs at once.
   3. With the relevant UFOs selected, click `Open` to run the copying.
7. Check the results, and save if desired. Close out of a font if you don't like the changes in it (and do not save).

## (Screencast: how to use Glyph Copier)

<iframe width="560" height="315" src="https://www.youtube.com/embed/y70jO-oXQfU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>