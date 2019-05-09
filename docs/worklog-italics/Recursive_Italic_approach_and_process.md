# Recursive Italic: approach and process

Earlier, [I considered what stylistic approach to take to italics](https://paper.dropbox.com/doc/What-kind-of-Italics-naxappNPTEF81CxJBPtPv). Now that I have decided to principally create a sloped-roman (including italic alternates, as is possible), I am trying to determine exactly *how* to make a good sloped roman: how to match color and appearance between upright and slanted characters.


## Question: what italic angle should I use?

Assumption: if I use an angle that yields a whole number of grid units (that is, over 1 unit, then up *x* units), it will be simpler to work with outlines, and it may render more nicely on pixel displays.

That makes for several possibilities:

- 11.31 degrees (Up 5, over 1)
- 14.04 degrees (Up 4, over 1)
- 18.43 degrees (Up 3, over 1)

Hypothesis: if I skew to a steeper angle and make optical corrections, interpolations will also have suitable corrections. I assume this is true because the optical issues introduced by skewing seem to be linear, rather than exponential. This may not be entirely true, if more complex characters require more drastic design changes to work in a heavy slope. Still, an initial test confirms that optical corrections made to an 18.43-degree slope appear to work pretty well in less intensive slopes (the width corrections may be slightly wrong, but the overall shape corrections seem to be working).


![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527432660437_image.png)


**Update, Jun 7: technical / engineering lettering often called for a slant of 15 degrees, historically. Maybe this is a good reason to use a 14.43 degree slant?**

https://www.typotheque.com/articles/from_lettering_guides_to_cnc_plotters


## Question: How should vertical stem thicknesses compare between upright and italics?

A natural problem is that when you mathematically skew a rectangle, the thickness of it is reduced.


![Thickness measured in vertical bar at 0°, then skewed to 11.31°, 14.04°, and 18.43°](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527414237149_image.png)



![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527425624172_image.png)


An 18.43-degree skew makes a rectangle or stem which is reduced in thickness by 5.122% – no matter the original width of the rectangle. This means that across font weights, stroke thicknesses will be recuced by the same percentage when skewed.

This distortion is even worse when you apply it to circular shapes. The top-right and bottom-left become much thicker, while the top-left and bottom-right become much thinner. Beyond uneven thicknesses, the shapes simply look different: the balanced oval becomes overly pointy

![Thickness measured in o at 0°, then skewed to 11.31°, 14.04°, and 18.43°](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527414506513_image.png)


Of course, accepting that stem thicknesses change from skewing, the next question is whether that matters, or whether it’s a bad or good thing for matching roman and italic styles.


## What are the goals of an italic? 

Generally speaking, an italic should:

- Provide emphasis and visual distinction to adjacent or surrounding blocks of upright text
- Visually match the weight of the surrounding upright text, which is a balance of matching: 
    - overall color on a page / screen
    - apparent stem thickness


## Testing how skewing affects color

Let’s test whether mathematical skewing affects the overall color of a page. Logically, it seems that skewing a series of rectangles shouldn’t affect the total area of black. This is confirmed by simple geometry (http://www.mathvillage.info/node/135).


![http://www.mathvillage.info/node/135](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527415642320_image.png)


This would seem to indicate that vertical stems *should* be thinner in italics, in order to maintain the same color. But, because type is visual and not simply mathematical, we should also test this ourselves rather than simply trust the math. 

I have set up a simple two-glyph test: one which doubles the vertical bar in order to evenly fill up glyph space, and a second which simply takes this and skews it to 18.43° (a 3/1 slope). 


![The first glyph of the test](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527415537730_image.png)
![The second glyph, skewed at 18.43°. These bars do look thinner…](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527415550784_image.png)



![A quick test in the RoboFont space center. At this size (this is a screenshot of 14px type on a retina screen), the text blocks appear to be the same overall level of gray to me…](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527415495109_image.png)



![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527416281076_image.png)



![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527416526275_image.png)

![8px mosaic](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527416609409_image.png)
![16px mosaic](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527416484305_image.png)

![32px mosaic](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527416576521_image.png)
![64px mosaic](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527416659227_image.png)


Drawbot test of the skew applied to Casual Regular `n` and `o`, using `gaussianBlur()` and `pixellate()` image filters

![screenshot of type at 14px](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527437233507_vscode-italic-test-nonono.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527422171947_vscode-nonono-blur-pixellate.gif)



## Problem: even though the color remains the same in a skewed version, the spacing gets tighter

But should this be solved before or after making the italics?

That is, it could be solved in one of two ways:

1. **Before skewing:** I could interpolate to get a slightly bolder copies of the masters, then reduce the widths of all letters to return to a similar stroke width, then skew. Done correctly, this should allow me to simply export italic masters at the same designspace settings as the roman masters. 
2. **After skewing:** I could make copies of the masters, reduce all character widths, skew all characters, and then make corrections. On exporting, I would then set interpolations to be a little bolder than the upright counterparts.



## What is the actual change in spacing?

Upright regular combo `nn` has 188 units of horizontal spacing. When skewed to 18.43, this becomes 178 units. At the 1000-unit working size, that looks like this:


![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527424345816_image.png)


As verified by a quick test in Adobe Illustrator, when letters have a skew of 18.43 degrees, there is a mathematical 5.32% reduction in spacing. This reduction is so close to the 5.122% reduction in the width of a skewed rectangle, it seems safe to say the difference is only coming from slight differences from exporting or usage in Illustrator. After all, the whitespace between `n` and `n` is just a rectangle.

Hypothesis: to counteract this loss of space while retaining overall text color, I need to:

1. Make an interpolation that has stems which are ~~5.122% thicker~~ 105.34% thicker, so they will be back to 100% when scaled down to 94.878% by the skew
2. reduce the horizontal width of characters by 5.122% (scaled to 94.878%) to make stems match origin again
![stems scaled to 105.34%, then character width scaled to 94.878%](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527431823982_image.png)

3. ~~correct horizontal stroke thicknesses to match original~~ to maintain proper appearance and optically similar counterforms, the horizontal strokes will need to be slightly reduced – i’ll try 94.878% to keep them in sync with the change of the verticals.
4. Skew to 18.43 degrees.


![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527431917736_image.png)

1. fix optical issues while attempting to maintain the same overall surface area.

Am I overthinking this? Quite possibly. The blurring of pixels in an italic font probably visually reduce italic spacing by a variable amount that depends on screen resolution and the rendering engine used. Much more obviously, I intend to change some details between the roman and italic, such as adding a few extra “tails” to letters. However, I do want to make a sloped-roman that is as “perfect” as possible, so even though this process will inevitably get corrupted, following it seems like a better starting point than simply skewing and hoping for the best.

**Results:**
After this … The color still matches quite well, and interpolation works decently between upright and italic. However, the italic ends up looking overly narrow and a bit more-widely spaced, and the strokes do seem to be a bit lighter-weight. It’s a bit hard to know how much of this is due to a flawed process, versus the natural result of such a heavy slant.



![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527433518900_image.png)
![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527433951086_image.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527434046146_image.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527434272785_image.png)


Let’s analyze the result. 

![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527434479325_image.png)


Perhaps I mixed up my process? In the skew-prepping drawing, just before the skew, the distance is be 201. This is scaled to about 94.787, or about 190 units. What would it need to be to be 185 units?

This can be figured out with `*x*` `* 0.94878 = 185`. There, `x = 194.98724678`. So, I will repeat the process, seeing where I can achieve total sidebearings of 195.

In the medium, once I’ve scaled both vertical stems by 105.34%, the total sidebearing is 179, while the glyph width is 421. This means the glyph must scale down by a total of 16 units, or by ~96.2%



![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527435550044_image.png)

![transformed to metrically match space between letters and also match overall surface area](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527435597647_image.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527435765743_image.png)


So, the process to slant letters while maintaining metrically similar sidebearings is:

1. horizontally scale vertical stems by 105.34%
2. vertically scale horizontal stems by 94.878%
3. scale new character width by 96.2%
4. skew result by 18.43 degrees
5. make remaining optical corrections to round shapes

Verifying that this actually works:

- If vertical strokes should scale by 94.878%, in the Medium weight, they should be 89.18532 units thick. However, they are now 89.95 and 90.88 units thick. 
    - However, the horizontal stroke has been made thinner, which wasn’t the case in the earlier simple skewing process. So, this probably somewhat offsets the minor difference of the stem widths.
- More importantly, does it look right? To be honest … it doesn’t quite look right to me. 


![Metrically-matching spacing between letters … might be too wide in italic](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527436954471_image.png)

![Metrically-matching spacing between letters … might be too wide in italic](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527437119011_image.png)



![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527436630884_vscode-morespacing-nenene-blur-pixellate.gif)


Now that I have found this formula, I need to determine two things:

1. Should I really slant to 18.43 degrees? I don’t think letters will typically be useful at such an extreme angle.
2. Is there a way to automate this set of instructions, so I don’t have to 


## Am I overthinking it?

Probably, yes. When a skew is applied, everything appears more narrow – not just stems, but also counters and sidebearings. By changing your process to keep any one of these the same as before, you are making the transformation *more* prominent in another metric. So, you can keep sidebearing “thickness” the same in roman and italic, *but* you will then be accepting more-narrow characters. This, then, makes sidebearings appear *wider* by comparison (also, letter stems tend to look thicker when more horizontal, and this likely holds true in spacing, not just strokes).

All this is to say … fuck it, I’ll skew without adjusting glyph widths, so that everything gets narrower at the same rate. Because horizontal strokes will need to be scaled down to match vertical changes, I accept that I may need to use interpolation to generate slightly-darker italic masters in the future, to once again match color. 


## 📯📯📯📯 Declaration of intent 📯📯📯📯

Skew prep will include:

- moving connection points to 0 or 90-degree positions, to allow better distortion correction
- scaling horizontal strokes by ~94.878% vertically, to proportionally match vertical distortions
    - this will mean light horizontals (about 50 units thick) will need to change by 
        - roughly 3 units in casual, and 
        - 2 units in gothic (which already has some correction)
    - bold horizontals will need to change by roughly 7–8 units in casual, and 7 units in gothic 
    - heavy horizontals vary a lot already, and will need to change by scaling, rather than nudging a fixed number of units (note: i may choose to not doing heavy italics…)

Skew cleanup will include:

- making NE and SW round areas less sharp
- making NW and SE areas less smooth
- possibly, exported instances will have slightly higher weights to match color, as needed.



## Next tests: using a core set of letters between all weights, mono and sans, to try to verify that a slope of 18.43 degrees is possible in a mono and duplexed typeface.

I’ll try `hamburg` for review with Paul, Monday

- this will allow for romans and a start into italic forms



![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527499299586_image.png)


Result of asking Paul: I need more context to know what’s working.

I could figure out how to make tests of these partial alphabets, *OR* I could just make the 11 reamining lowercase letters in the core mono fonts, then have something realistic to test with. This seems more useful, especially with the thursday presentation deadline.



## How are the italics influencing the romans?

I have quite a few letters with connections are 45 degrees. It looks nice as an overlap and it doesn’t cause *too* much trouble in upright letters, but it makes italic versions very challenging to draw well. So, I am editing most of these instances out of the uprights in order to make these curves better.


![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527514933382_image.png)
![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527514915167_image.png)



## Future work: evening out corner curves
![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527517552327_image.png)



## Mono Lowercase first draft, done!

I will now copy these corrected letters into the skewed full-charset mono UFOs, in order to test everything, with a special focus on the readability / usability of the lowercase.


![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527523912537_image.png)


I did try to take this through my font-generation method, but for some difficult-to-determine reason, it will generate a variable font with slant, but it will not generate instances with slant. 😐 

Well, giving my lack of time, I need to be satisfied with the fact that things are mostly working in superpolator, and do as many Sans corrections and italicizing tasks as I can for thursday.


## Italic alternates

first round

- a (could be more humanist on top)
- f
- g (could also be more humanist on top)
- i 
- l
- r (make these hookless)
- y



maybe

- q? (could be more humanist on top)

I’ve considered even more italic alternates, which i could introduce as time allows:

- k
- v
- w
- z
- j
![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1527534303966_image.png)



## Should it be a “rotalic”??

In early tests, I’ve simply skewed and corrected letters. This is likely the right approach for the Gothic style, but it doesn’t make much sense for the casual, which tries to approximate brush strokes more closely.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1528028191445_image.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1528028204580_image.png)


To me, the casual style certainly looks better as a rotalic, but it will take longer to make …

Meanwhile, I am super tempted to make a “rotalic” gothic, but the readability of it suffers greatly – lines of text lose a lot of cohesion, because the baseline and x-height become so broken up. I love the look of it, but it’s probably not right for the core product, as the theme of the gothic style is simplicity and readability.


![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1528030407839_image.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1528029273889_image.png)

## Style-linking

I was having style-linking issues. I don’t yet know how to automate this, but it seems to be caused by the name tables in the exported TTFs, due to values which are explained at https://docs.microsoft.com/en-us/typography/opentype/spec/name


## Upgrades
[ ] `a` should definitely get a tail for added legibility



## Should the slant really go up to 18.43 degrees? Probably not.

Previously, I slanted and corrected to 18.43 degrees, then exported instances at 14.04 degrees. I like this slant because it is closely related to old manuals for technical lettering (which commonly recommended 15 degrees, likely for geometric simplicity), it is distinctive, but it is not *too* extreme. 

This is a screenshot of proportional type in a text editor, simply because I corrected style-linking in the proportional and not yet the mono. It shows that 

**The exported italic angle of 14.43 is already quite significant:**


![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529232564067_image.png)


**14.04 degrees is already a distinctly heavy slant for modern type:**

![versus the usual Atlas Grotesque, in Dropbox Paper](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529234058493_Large+GIF+1090x706.gif)

![Compared against several common typefaces](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529233623266_image.png)


**If I use an interpolation as the primary italic, I will be extending my range but sacrificing quality control**
Drawing at 18 degrees but exporting to 14 degrees might mean that the italic has many little issues. If I directly draw the italic, I will be able to correct those, and issues that show up in intermediates will be far less-commonly seen. 


## 📯📯📯📯 Improved intent for 14-degree slope 📯📯📯📯

Skew prep will include:

- moving connection points to 0 or 90-degree positions, to allow b````etter distortion correction
- scaling horizontal strokes by ~94.878% vertically, to proportionally match vertical distortions
    - this will mean light horizontals (about 50 units thick) will need to change by 
        - roughly 2 units in casual, and 
        - 2 units in gothic (which already has some correction)
    - bold horizontals will need to change by roughly ~~7–8 (?)~~ **5** units in casual, and 7 (?) units in gothic 
    - heavy horizontals vary a lot already, and will need to change by scaling, rather than nudging a fixed number of units (note: i may choose to not doing heavy italics…)

Skew cleanup will include:

- making NE and SW round areas less sharp
- making NW and SE areas less smooth
- possibly, exported instances will have slightly higher weights to match color, as needed.




## How to correct Italics

I was really struggling to correct the italics after starting by skewing them  – especially the Casual, in the lightest weight. It stacks up several big challenges:

- The structure of my typeface is such that the sides of round letters have two extreme points, so that they can interpolate into the gothic / stricter weight. These are simple enough to work with in the upright versions, where they can simply be vertically-aligned. In the slanted version, however, they tend to start as a kinked line as soon as coordinates are rounded. The line can be made smoother by giving them more distance from one another, but this lead to two problems. First, the letterform tends to get boxy if these points are moved further apart. Second, the more their positional relationship is changed from the upright, the worse the kinking is in interpolation between upright and slanted masters. 
- It’s hard to correct a skewed ellipse in a geometric typeface, and indeed, I’m having less trouble handling my “strict” slanted masters. I believe this is because it is relatively simple to know what a geometric italic should look like, because I see this style all the time. However, what should an egg-shaped `o`  look like when slanted? It’s very challenging to make this balance … every thing seems to look wrong


![How does one slant an egg-shaped o?](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529262772251_Screen+Shot+2018-06-17+at+9.12.17+PM.png)


I’ve found one thing extremely useful for the process of correcting my italics: using the extension “Ground Control” on a secondary screen, in order to see each letter in the context of it neighbors as well as how it relates to the upright. This extension has a slightly confusing set of controls, but by clicking the “remove” button to reduce the visible masters, then clicking “all controls” to view the font-selection menus, it can be controlled. Seeing the italics just above their roman counterparts makes it much, much easier to judge whether they are being curved in the right way.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529263036122_Screen+Shot+2018-06-17+at+9.17.02+PM.png)


I’ve been keeping the italics in the non-slanted box view, because I was worried that it appeared off-center. However, this article is helpful in showing how to use RoboFont’s “Italic Offset” feature to correct for that: http://robofont.com/documentation/how-tos/working-with-italic-slant/




![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529265755020_Screen+Shot+2018-06-17+at+10.02.05+PM.png)


In order to minimize the amount of kinking in interpolated instances of the typeface, I am moving paths in a slightly unusual way. Instead of dragging handles, I am making extensive use of the transform tool (shortkey `T`). That is, on an angle set of handles, instead of dragging the right handle up and to the right, I would select the main point with its handles, then transform the whole unit up and to the right.  This helps keep the ratios of handles in sync between masters, which allows them to interpolate as a “unit” rather than separately. 

I am also working on a slanted grid of guidelines, which I toggle on and off to make sure handle angles match the overall slant, while allowing the letterform to be correct.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529310674494_Screen+Shot+2018-06-18+at+10.30.42+AM.png)


I am using the extension Ground Control to position the slanted letters above their roman counterparts, then watching this window a lot as I make corrections. I am keeping several things in mind:

- aiming for optically-matching curves
- aiming for optical balance of the left and right sides of the slanted letters
- aiming to maintain the same relative stroke thicknesses
![Here, corrections have been made to the 0 and 1; the 2 is in progress, and the others are yet to be fixed](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529310927736_Screen+Shot+2018-06-18+at+10.31.01+AM.png)



![italic-optical_corrections-061818.at](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529312557815_image.png)



## Integrating corrected italic characters into var-font ready fonts
1. Copy each roman font
2. Update font info to make italic: style name, italic angle, and italic offset
3. Script the skewing for all letters
4. copy in the corrected forms


[x] casual A
[x] casual B
[x] gothic A
[ ] gothic B

Ohhh crap. The script was *seeming* to work, but just because it was decomposing everything before running. However, doing this would mean that the corrections to letters won’t cascade through component glyphs (all the diacritics).

So, what I’m getting is not what I want:

![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529315623027_image.png)


But if I simply leave out the `decompose()` step, this happens:


![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529315583009_image.png)


Luckily, Frederik has already written a script that accounts for components, which is at http://robofont.com/documentation/how-tos/working-with-italic-slant/?highlight=italic%20offset … I need to start with this, but modify it to *slant* all glyphs, as well as anchors, and account for components.




## Correcting sidebearings of corrected italics

Because I started my italics before understanding how RoboFont uses the `italicAngle` and `italicOffset`, my glyphs are spaced a bit randomly. However, because they are simply corrected versions of glyphs in the upright fonts, I should be able to script the sidebearings from the upright into the slanted version with `g.angledLeftMargin`.



## Correcting placement of anchors in italics

The anchors were copied in before skewing glyphs, but then weren’t skewed along with the glyphs. I could go through manually and place them better, but it would be more useful to do this in script, so it’s faster – especially because I don’t yet have actual accents to position over the italics, anyway, so I’d have to fix it later, anyway.

I was thinking I would have to use “ray,” but it already has an x position. I can just sync those! Not so bad.

…actually, x position is a bit mess up in italics. Just asking for an x-position gives it an x-position based on the baseline.

So, I ended up using some trigonometry to calculate the proper x position of the anchor, based on the italic angle and the y position from the upright version.

However, it’s so close to the end of the semester, I probably have to scale down my goals for what will be included in the variable font, and what will be in instances, instead.


## Bringing corrections into sans italics

Now that I have mono italics, I also want sans italics.

I’ll use my glyph-copying script to bring in the letters and figures I’ve already worked on, then add in the rest.

I interpolated this 14-degree sans from the earlier 18-degree sans italic and the current upright sans, then copied into already-corrected, normal-width mono characters. This means that there are still some characters to correct: everything in red (these are the sans-specific characters), plus, of course, the missing characters. There are quite a few here, because:

1. I only had lowercase for the greenlight presentation
2. I’ve changed the connections on some of these characters since the greenlight presentation, making them incompatible with the uprights
3. 




![](https://d2mxuefqeaa7sj.cloudfront.net/s_24F0F1DE8ACA15A1F30F3F7AD0EF912FCA517F93771A86416C619D630DDDEA57_1529359170469_image.png)


I deleted a bunch of characters with this:

    letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z zero one two three four five six seven eight nine a.italic f.italic g.italic i.italic l.italic r.italic y.italic"
    
    glyphList = letters.split()
    
    # help(CurrentFont())
    
    for g in CurrentFont():
        if g.name not in glyphList:
            # g.selected = True
            CurrentFont().removeGlyph(g.name)

