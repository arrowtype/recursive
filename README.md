# Recursive Mono & Sans

![](specimen.png)

Recursive Mono & Sans is a variable type family built for better code & UI. It is inspired by casual script signpainting, but designed primarily to meet the needs of programming environments and application interfaces.

In programming, “recursion” is when a function calls itself, using its own output as an input to yield powerful results. Recursive Mono was used as a tool to help build itself: it was used to write Python scripts to automate type production work and to generate specimen images, and it was used in HTML, CSS, and JS to create web-based proofs & prototypes. Through this active usage, Recursive Mono was crafted to be both fun to look at as well as deeply useful for all-day work.

Recursive Sans borrows glyphs from its parent mono but adjusts the widths of many key glyphs for comfortable readability. Its metrics are *superplexed* – every style takes up the exact same horizontal space, across all styles. In this 3-axis variable font, this allows for fluid transitions between weight, slant, and “expression” (casual to strict letterforms), all without text shifts or layout reflow. Not only does this allow for new interactive possibilities in UI, but it also makes for a uniquely fun typesetting experience.

## Variable Axes

Recursive is still being built, but it will have the following axes:

| Axis       | Tag  | Range        | Default | Description                                                     |
| ---------- | ---- | ------------ | ------- | --------------------------------------------------------------- |
| Proportion | PROP | 0 to 1       | 0       | Fixed-width or Natural-width (or something in between)          |
| Expression | XPRN | 0 to 1       | 0       | Linear to Casual                                                |
| Weight     | wght | 300 to 900   | 300     | Light to Heavy. Can be defined with usual font-weight property. |
| Slant      | slnt | 0 to -15     | 0       | Upright (0°) to Slanted (about 15°)                             |
| Italic     | ital | 0, 0.5, or 1 | 0.5     | Always roman (0), auto (0.5), or always italic (1)              |

Note: `PROP` and `XPRN` are "unregistered" axes (not currently in Microsoft's official listing of variation axes and specs), so these tags must be used in all-caps in CSS, etc.

<!-- 
## Build


To build, set up the virtual environment

```
virtualenv -p python3 venv
```

Then activate it:

```
source venv/bin/activate
```

Then install requirements:

```
pip install -U -r requirements.txt
```

(...to be continued) -->

## Collaborators 

- Stephen Nixon
- Lisa Huang
- Katja Schimmel
- Rafał Buchner

+ Many other advisors and reviewers
