from mojo.UI import OutputWindow

g = CurrentGlyph()

OutputWindow().show()

firstColWidth = 18

print("")
print(g.name)
print("".ljust(96, "-"))

for f in AllFonts():

    print(f.info.styleName.ljust(firstColWidth + 1), end=" ")
    print("|", end=" ")
    for anchor in f[g.name].anchors:

        print(anchor.name, end=" ")

    print("")
