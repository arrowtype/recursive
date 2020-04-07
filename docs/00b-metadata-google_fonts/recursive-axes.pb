axis {
  tag: "MONO"
  display_name: "Monospace"
  min_value: 0
  max_value: 1
  default_value: 0
  precision: -2
  fallback {
    name: "Sans"
    value: 0
  }
  fallback {
    name: "Mono"
    value: 1
  }
  description:
    "Adjusts the typeface from Sans (proportional/natural width letters, default) to Mono (monospace/fixed width)."
	"Proportionally spaced fonts have letters "
    "drawn with more typical proportions, and each glyph takes up a unique "
    "amount of space on a line."
    "Monospace is when all glyphs have the same space total character"
    " width, and more wide or narrow letter proportions to fill the space such"
    " as a narrow 'w' or wider 'r.' 
}
axis {
  tag: "CASL"
  display_name: "Casual"
  min_value: 0
  max_value: 1
  default_value: 0
  precision: -2
  fallback {
    name: "Linear"
    value: 0
  }
  fallback {
    name: "Casual"
    value: 1
  }
  description:
    "Adjusts the typeface from Linear (rational shapes, default) to  Casual (brushy)."
	"The Linear style merges aspects of humanist sans with rationalized, compact, "
	"flat-sided letterforms. This regular, familiar structure makes it appropriate "
	"for long-form text requiring focus (e.g. paragraphs, full code documents, and "
	"punchy headlines). The Casual style is inspired by single-stroke casual "
	"signpainting, but drawn for small sizes. It is most useful in shorter-form text "
	"where a warm and inviting tone is desired (e.g. blog post headlines, store "
	"signage, and computer terminals)."
}
axis {
  tag: "wght"
  display_name: "Weight"
  min_value: 300
  max_value: 1000
  default_value: 300
  precision: -2
  fallback {
    name: "Light"
    value: 300
  }
  fallback {
    name: "Regular"
    value: 400
  }
  fallback {
    name: "Medium"
    value: 500
  }
  fallback {
    name: "SemiBold"
    value: 600
  }
  fallback {
    name: "Bold"
    value: 700
  }
  fallback {
    name: "ExtraBold"
    value: 800
  }
  fallback {
    name: "Black"
    value: 900
  }
  fallback {
    name: "ExtraBlack"
    value: 1000
  }
  description:
    "Adjust the overall thickness of letters and the darkness of text composed with "
	"them. Notably, in Recursive, the weight axis does not affect glyph width. A bold "
	"weight takes the same amount of space as a light weight, even at in proportional "
	"styles of the MONO axis."
}
axis {
  tag: "slnt"
  display_name: "Slant"
  min_value: -15
  max_value: 0
  default_value: 0
  precision: -2
  fallback {
    name: "Upright"
    value: 0
  }
  fallback {
    name: "Italic"
    value: -15
  }
  description:
    "Adjusts the forward lean of letters. -15 (negative 15) corresponds to a 15-degree "
	"clockwise slant, due to type design's roots in geometry. If the Cursive axis is at "
	"its default value, going past a slant of -13.99 will activate cursive letters, "
	"converting them to more-handwritten forms such as the simplified, single-story "
	"a and g."
}
axis {
  tag: "CRSV"
  display_name: "Cursive"
  min_value: 0
  max_value: 1
  default_value: 0.5
  precision: -1
  fallback {
    name: "Auto"
    value: 0.5
  }
  fallback {
    name: "Roman"
    value: 0
  }
  fallback {
    name: "Cursive"
    value: 1
  }
  description:
    "Controls the substitution of cursive forms along the Slant axis. 'Off' (0) "
	"maintains Roman letterforms such as a double-story a and g, 'Auto' (0.5) "
	"allows for Cursive substitution, and 'On' (1) asserts cursive forms even in "
	"upright text with a Slant of 0."
}