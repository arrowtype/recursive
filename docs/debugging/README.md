# Debugging "Line can not have an offcurve"

In running varfontprep, I started running into this error:

> <class 'fontTools.ufoLib.errors.GlifLibError'>: line can not have an offcurve.

This came after merging https://github.com/arrowtype/recursive/pull/271, a PR to make superiors/inferiors/fractions more legible at text sizes.

So, the problem probably came either from a merge issue or from ... some kind of RoboFont bug, possibly?

## Finding the source of the bug

I added some `print()` statements into varfontprep to discover which glyph was crashing the process. It seems that it was `src/masters/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif`. So, I made a new, specific UFO to test just this glyph.

I copied the XML code from this file into a glif file of the new UFO, then played around to find the issue. It seems that mostly, it was the following:

```XML
    <point x="266" y="667"/>
    <point x="301" y="695"/>
    <point x="402" y="628" type="line"/>
```

These were two offcurve points leading to a `type="line"`. All other similar instances led to `curve` points. Changing it to `curve` makes it possible to open the file in RoboFont without crashing the app.

However, this doesn't entirely fix it ... the code-edited glyph just doesn't show up in RoboFont, currently, if I try to open its glyph window.

## Going back in (Git) history

I'll try checking out an earlier version of this offending file, to see whether I can find a previous version without the problem. I started by making a branch:

```
git checkout -b "fixing-curves-zerosuperior_dotted"
```

I ran git log:

```
git log -- "src/masters/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif"
```

...and then copied the hash for Lisa's last commit on this file:

```
git checkout 3fda3d2dd8 -- "src/masters/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif"
```

And sure enough, it opens into RoboFont with no problem.
