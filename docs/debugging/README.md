# Debugging "Line can not have an offcurve"

In running varfontprep, I started running into this error:

> <class 'fontTools.ufoLib.errors.GlifLibError'>: line can not have an offcurve.

This came after merging https://github.com/arrowtype/recursive/pull/271, a PR to make superiors/inferiors/fractions more legible at text sizes.

So, the problem probably came either from a merge issue or from ... some kind of RoboFont bug, possibly?

## Finding the source of the bug

I added some `print()` statements into varfontprep to discover which glyph was crashing the process. It seems that it was `src/ufo/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif`. So, I made a new, specific UFO to test just this glyph.

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
git log -- "src/ufo/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif"
```

...and then copied the hash for Lisa's last commit on this file:

```
git checkout 3fda3d2dd8 -- "src/ufo/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif"
```

And sure enough, it opens into RoboFont with no problem.

Merging these fixes back into master, I see the issue:

```
src/ufo/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif | 20 --------------------
```

Basically, 20 extra lines had made their way into the glyph.

Opening the `Sans Casual C Slanted` UFO again, it works! No RoboFont crashes this time.

## Probable cause of the problem

When I merged Lisa's latest PR into Master, there were many merge conflicts – mostly in `lib.plist` files. 

I've found that so far, I've been able to just "accept both changes" to resolve these `lib.plist` merge conflicts – because they keep being simply from glyphs being added by both of us, and RoboFont seems to sort through any duplicates if they are introduced.

The _fastest_ way of "accepting both changes" is to find and replace Git's merge conflict markers, which are something like `<<<<<<<<HEAD`, `==========`, and `branch>>>>>>>>`. 

However, I did _not_ limit this find-replace operation to `lib.plist` files, which probably merged a conflict in the `zerosuperior.dotted.glif`.

## Checking for similar problems

I need to check whether there might be any similar problems lurking from my sloppy merge. It's not immediately apparent how to do so, but I'm sure Git makes this possible...

Basically, I need to find what files were merged with this:

```
commit a0f5f7445a94f6f021ee2212a938edc43e308278 (fractions-legibility)
Merge: 3fda3d2dd8 27a0b02fe3
Author: Stephen Nixon <stephen@thundernixon.com>
Date:   Sat Dec 14 18:06:19 2019 -0500

    Merge branch 'master' into fractions-legibility
```

...and how many didn't have a filename including `lib.plist`.


This took some experimentation, but I found that the following format could work:

```
git diff 3fda3d2dd..a0f5f7445 -- 'src/ufo/sans/*zerosuperior.dotted.glif'
```

This was `git diff` then `<commit before merge>..<commit after merge>` then `-- '<path with wildcards, in quotes>'`.

...buuut even though it showed me interesting details of the merge, it didn't provide an easy answer as to which files had merge _conflicts_.

Instead, I Googled it and realized that I should just re-run the merge: https://stackoverflow.com/a/15443923

> Yes, it is trivial. First of all, you need find sha1 id of the merge commit using git log. When you do the next:
> 
> git checkout <sha1>^1
> git merge <sha1>^2
> you will be in a headless state. ^n means n-th parent of a commit. So, no branches are created. You could resolve conflicts again more carefully and then
> 
> git diff HEAD..<sha1>
> to see if there are any differences in the conflict resolutions.

I could then run `grep` to see which files had merge conflict syntax:

```
▶ grep -R "<<<<<<< HEAD" *
src/ufo/sans/Recursive Sans-Linear B Slanted.ufo/lib.plist:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Linear A Slanted.ufo/lib.plist:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Casual C.ufo/lib.plist:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Casual B.ufo/lib.plist:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Casual A.ufo/lib.plist:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Casual C Slanted.ufo/lib.plist:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Linear C Slanted.ufo/lib.plist:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Casual A Slanted.ufo/lib.plist:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Casual B Slanted.ufo/lib.plist:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Linear A.ufo/lib.plist:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Linear C.ufo/lib.plist:<<<<<<< HEAD
src/ufo/sans/Recursive Sans-Linear B.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Casual A.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Casual B.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Casual A Slanted.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Casual C.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Linear C Slanted.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Casual B Slanted.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Linear B Slanted.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Linear B.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Linear C.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Linear A.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Casual C Slanted.ufo/lib.plist:<<<<<<< HEAD
src/ufo/mono/Recursive Mono-Linear A Slanted.ufo/lib.plist:<<<<<<< HEAD
```

And, this confirms that `src/ufo/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif` was the only glyph with a conflict!

Good to know.

I got out of this detached HEAD state with `git merge --abort`, then `git checkout master` (https://stackoverflow.com/a/11801199).
