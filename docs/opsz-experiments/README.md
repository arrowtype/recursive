# Experiments with Optical Sizing & "Binary" Variation Axes

Goal: Make a font which has: 
- A large range of flexibility.
- Safegaurds to prevent poor usage.
- Maintains a compact file size.

I'll be taking a quick look at each of these goals.


## A large range of flexibility

Recursive Mono & Sans has several variation axes:
- Weight: from Light to (very) Heavy
- Slant: from upright to 14.04° of forward slant
- Italic: alternate letterforms which can either be within their own axis or tied to the Slant axis
- Expression: (Casual (curvy) versus Linear (normal) letterforms)
- Proportion: Mono vs Sans (coming soon)

Between these axes, there is a huge amount of room for users to play with typographic styles.

## Safegaurds to prevent poor usage.

Not all possible combinations are equally as refined for large usage, where slightly rounding issues can disrupt the quality of interpolated glyph outlines.

A common issue is "kinking."



The “expression” axis is meant to be fluid, but middle values aren’t recommended above 24px or so.
A “binary” axis can be achieved like this

```
source A
- expression: 0

source A
- expression: 0.4999

source B
- expression: 0.5

source B
- expression: 1
```


## Maintains a compact file size.