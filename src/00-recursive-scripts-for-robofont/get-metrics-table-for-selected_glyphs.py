font = CurrentFont()

glyphsToGetMetricsOf = font.selectedGlyphNames

print("| glyph | width | LSB | RSB |")
print("| :--- | :--- | :--- | :--- |")
for name in glyphsToGetMetricsOf:
    g = font[name]
    print(f"| {name.ljust(20)} | {g.width} | {g.leftMargin} | {g.rightMargin} |")
    