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

Merging these fixes back into master, I see the issue:

```
src/masters/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif | 20 --------------------
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
git diff 3fda3d2dd..a0f5f7445 -- 'src/masters/sans/*zerosuperior.dotted.glif'
```

This was `git diff` then `<commit before merge>..<commit after merge>` then `-- '<path with wildcards, in quotes>'`.


```
diff --git a/src/masters/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif b/src/masters/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif
index 97ba4da305..2ef14d0b74 100644
--- a/src/masters/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif      
+++ b/src/masters/sans/Recursive Sans-Casual C Slanted.ufo/glyphs/zerosuperior.dotted.glif      
@@ -55,6 +55,26 @@
                        <point x="249" y="599" type="line" smooth="yes"/>
                        <point x="266" y="667"/>
                        <point x="301" y="695"/>
+                       <point x="402" y="628" type="line"/>
+                       <point x="397" y="633"/>
+                       <point x="392" y="635"/>
+                       <point x="385" y="635" type="curve"/>
+                       <point x="373" y="635"/>
+                       <point x="361" y="621"/>
+                       <point x="350" y="579" type="curve" smooth="yes"/>
+                       <point x="329" y="496" type="line"/>
+                       <point x="333" y="492"/>
+                       <point x="339" y="490"/>
+                       <point x="345" y="490" type="curve" smooth="yes"/>
+                       <point x="358" y="490"/>
+                       <point x="372" y="507"/>
+                       <point x="379" y="535" type="curve" smooth="yes"/>
                </contour>
        </outline>
+       <lib>
+               <dict>
+                       <key>public.markColor</key>
+                       <string>1,0.5,0,1</string>
+               </dict>
+       </lib>
 </glyph>
 ```

 https://stackoverflow.com/questions/11048094/git-get-conflicts-from-past-merge-without-running-merge-once-again