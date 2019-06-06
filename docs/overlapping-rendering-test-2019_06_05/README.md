# Testing overlap rendering on medium to low-DPI screens

**Date: June 5, 2019**


## Question

Does glyph construction matter for text rendering on medium to low-DPI screens?

Clearly, prior experience in Recursive has shown that "exterior" overlaps often render poorly on low-DPI screens. Take an "o" that is made up of two halfs, overlapping but smoothly connecting on the top and bottom. Antialiasing happens on both of the overlapped contours, but if the top edge of one turns on a pixel at 50% gray at the top of both contours, these values *add up,* resulting in a terrible blobby lettershape at small scales, and less-distracting but still-noticeable bumps at larger sizes.

![](assets/2019-06-05-22-13-05.png)

*Above: rendering issue with overlapping contours, as seen in Chrome browser on macOS. Arrows point out examples of the rendering issue.*

BUT, does this also effect the rendering of *"interior"* overlaps? 

Variable font can retain overlapped contours, and this is very useful to draw glyphs efficiently for interpolation. But do they face this issue in all contours? Examples of "interior" overlap are:
- The crossbar of a /t, made from a separate rectangle crossing a stem
- The are where a bowl or curve joins into a stem, on letters like /d, /e, /a, or /n.
- A corner which is not a simple acute angle, but two overlapped paths that connect in a loop, as is frequent in a letter like /M
- Areas in which "ink traps" are made by overlapping a small rectangle over the inner corner of a joint.

![](assets/2019-06-05-22-20-21.png)
![](assets/2019-06-05-22-20-35.png)
![](assets/2019-06-05-22-20-51.png)
![](assets/2019-06-05-22-21-17.png)

It appears to happen, though thankfully in a less-noticeable way. 


## Testing

I've made a very simple VF, `variable_ttf/overlap-tester-VF.ttf`. This puts contours for /d, /e, and /l into the spots for /a through /i, each in three different styles of drawing. This was then built with FontMake.

![](assets/2019-06-05-22-45-48.png)

![](assets/2019-06-05-22-46-47.png)

![](assets/2019-06-06-15-15-30.png)

*Interestingly, either FontMake or Sketch are removing some overlap from the first "e," even though that overlap is present in the UFO.*

This is tested in `index.html` of this directory, which can be opened directly in any browser. I am looking at it in Chrome.


## Results

Variable font, macOS 10.14.5, Chrome 74, Dell P2419H (Pixel per Inch (PPI) 92)

![](assets/overlap-test-screenshot.png)

![](assets/overlap-test-screenshot-windows.png)

## Conclusions

Whereas the problems from exterior overlap in contours were extremely apparent at many font sizes, this test shows little to no perceivable difference in rendering for interior overlap. 

I was particularly concerned with whether there would be dark patchs in the bowl of the /d, where the strokes joined the main stem, with overlapping recangles in the "complex overlap" version. Below, circled in green, are instances of the "issue" that concerned me, in each style of overlap.

![zoomed-in view of rendering imperfections of letter d at 14 and 16 px](assets/2019-06-06-15-46-17.png)


Perhaps, looking that the 14px letters, there is a *very slight* advantage gained by removing overlap. However, this is so neglible, I can barely tell, even at this extremely zoomed-in view. Most readers will not be looking this closely at such small sizes, and most will be a lot less attuned to this issue in the first place.

However, even if removing all overlap in production made a noticeable difference for some renderers, this has two primary counterarguments:

1. Rendering technology will change, and the current trend of increasing resolutions will continue. Rendering issues of any kind are much harder to percieve at higher resolutions – anything above 150 PPI or so makes even exterior overlap issues very hard to see.

2. Drawing interpolating letters without overlap would be very honerous and slow down the entire process. A type design workflow must optimize for more than just rendering: it must meet time contraints and remain flexible enough to allow for design refinments along the way. Removing all overlap may restrict interpolation severely, but worse, it would give less control to path refinement and require quite a lot more time to draw related glyphs (e.g. /n and /h, /d and /q, etc). 