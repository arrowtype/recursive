# Major stages & decisions in recursive

_Written by Stephen Nixon_
_Edited by Noemi Stauffer_

Recursive is a very personal project, but one which I think many people can benefit from.

## Before

- Grew up living letters. Excited to learn graphic design was a career path. Went to school for it. Excited to learn type had a career path, and programs like TypeMedia existed.
- After undergrad, IBM Product/brand designer, lettering/fonts on the side
- I love to code (especially for the web). I love making fonts. Both are magical-feeling ways of taking ideas and making them interactive and infinite.
- Recursive was a way to combine the things I love. I made it in RoboFont, a font editor that is slightly intimidating for newcomers, but really encourages customization of one's workflow with scripts, extensions, and the split-up UFO file format

## Context

- TypeMedia is... (Explain basic legacy and semester 1 variety)
- TypeMedia is known for producing projects that are experimental, but often very rooted in the idea of type coming from handwritten strokes. Often, projects include styles for both display and text.
- Outsiders tend to think of fonts in a way that is very limited, and largely driven by a "Microsoft Word" categorization of type: one style in "RIBBI"
- Historically, type had different styles for every size, sure in part to the tools of punch cutting, but also to knowledge of the human reader. Many styles were combined within compositions (show examples?)

## Start

- Sketching the idea. Wanting to do many styles in a big monospace family.
- Based this on "casual script," a style of signpainting that I've long been enamored with, and wanted to learn more about
- Prototyping atop Plex mono to test the idea. I also tested another totally different idea (which I still intend to make as a future project), but ultimately went with this weirder one. YOt]mO
- Scrapping the prototype, but largely keeping the metrics to stay consistent with other mono fonts. Allows fallbacks during design phase
- Early drawings. Searching for something both expressive and simple/typographic. Tried to explore this by making something too wild, and something too rigid. Realized that having a spectrum was more interesting than finding just one thing in the middle.

## Development at TypeMedia

- Inventing my own casual alphabet, with different brushes and pens. Taking uppercase forms into a roman lowercase.
- Narrowing focus. Experimenting with connected scripts and blackletters, but leaving these aside out of (a small amount) of practicality
- Expanding weight range. The heavy was too good to ignore. Most type designers say that the weight range of monospace designs are limited by what complex characters can do. I disagree. 😈 "Sporklike" contrast and overall color
- Finding the right balance of personality and typographic harmony
- Making curviness match between letters like /n and /o – finding that low connections and bouncy contrast could help with this
- Made a chrome extension to inject my font into any page, and read with it. (This has since been turned into Type-X, a very useful and much faster version of what I made – thanks, @PixelAmbacht).
- Paying attention to text rendering by using the fonts. Smoothing kinks from Linear styles to make them as seemlessly readable as possible – avoiding visual "breaks" or whitespots in letters
- Making a sans by scripting some Glyphs to copy over but leaving others to draw/adjust
- Producing materials for the TypeMedia thesis: specimens, poster, process book, and a simple web type tester

Post TypeMedia

- Further developing the recursive minisite as a way to better understand react/Gatsby, and as a better way to show the project to others
- Making my TypeMedia class website

## Google fonts project

- I was ready working on variable font upgrades and onboarding, to upgrade existing fonts like Encode, and onboard new, popular fonts like Fira Code and Inter. During this, Google Fonts offered to sponsor my project, to make it happen sooner and be available as an open-source font.
- Google Fonts is somewhat controversial. Does it devalue the industry to have so many free options?
- For Recursive, OFL and Google Fonts was ideal. This typeface is for coders of all abilities and experiences, open-source code docs, and to push new ideas forward in variable type on the web, software, and end users. It could be a niche product that i made a side project for 5 years, or it could make an impact and be published within 2019. There are still tons of benefits in favor of buying non-open type. Operator and Input are _masterful,_ classic designs. I am not trying to replace them, but rather, to push the wider typographic environment to be more interesting and expressive.
- I knew I needed to remove some overlaps to improve text rendering. Should I change it more than this?
- One designer's advice: "don't change it much. Use your new ideas on future projects."
- Another designer: "do you think you will really have the freedom you want if you publish through Google fonts?"
- Me: decides to add a bunch more cursive italics, more curves to all slanted forms, inktraps all over, remove problematic overlaps, and refine everything. And code ligatures.
- Luckily, I was able to get help from some awesome collaborators. Katja, Lisa, and Rafał.
- Cursive letters
  - for a more fun and unique italic. Bringing these from a stylistic set into their own ital axis, for easier control and less font weight than stylistic sets.
- Curvy slanted forms
  - for an even wider range of expression. Kept horizontal curves flat, but put curves into all vertical strokes to better follow the movement of a brush.
- Inktraps – How hard can they be?
  - Answer: very hard. Inktraps seem like a small decision, but actually, inktraps are very challenging to do right. How big should they be? How consistent in size? Angle? What about in different Glyphs? Different masters?
- Removing overlaps, for better rendering at text sizes
  - During TypeMedia, I drew Recursive in such a way that took the idea of designing with "The Stroke" in mind very literally. However, I realized right after TypeMedia that while this approach did enhance my design approach in some ways and gave me flexibility to think differently about what I was drawing, it had a critical flaw in use: overlaps showed up as little "blobs" on the outlines of letters, leading text to be subtly distorted in an unflattering way.
- Refinements
  - Things were drawn quickly at TypeMedia, so tons of things were bothering me. Lumpy curves, asymmetrical glyphs that should be symmetrical, not-quite ideal proportions, almost no kerning in sans beyond a proof of concept.
  - Rafał helped develop two important tools
    - Master compatibility, to help find and correct incompatible glyph drawings
    - Glyph Mirror, to make it much faster to draw symmetrica contours where desired
- Code ligatures
  - Controversial among type designers. But in a Twitter poll, 21% of 700+ respondents said they "wouldn't code without em"
  - Why are they useful? They are like syntax highlighting. They help coders to see that they have typed the right thing in the moment, and to visually scan their code more easily later on
  - Worked with rafał on early designs of this. Principles: better chunking, more recognizability, and improving legibility.
  - Crowdfunding this part so Rafał and I can finish these. Google will match contributions!
