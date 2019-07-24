from mojo.UI import OutputWindow

g = CurrentGlyph()

OutputWindow().show()

firstColWidth = 18

print("")
print("FONT".ljust(firstColWidth + 1), end=" ")
print("|", end=" ")

key = "| 🥐 = curve | 📏 = line | 🚚 = move | 🥨 = qcurve"
print(f"Contours & segments in /{g.name} {key}")

print("".ljust(firstColWidth + 1, "-") + " | " + "".ljust(96, "-"))

for f in AllFonts():

    print(f.info.styleName.ljust(firstColWidth + 1), end=" ")
    print("|", end=" ")
    counter = 0
    for c in f[g.name]:
        print(f"C{counter}", end=" ")
        print(f"[{len(c.segments)}]", end=" ")
        for s in c:

            # possible segment types: move, line, curve, qcurve

            # if you want to be boring:
            # print(s.type[0].upper(), end =" ")

            # if you want to spot the differences more easily:
            if s.type == "line":
                print("📏", end=" ")
            elif s.type == "curve":
                print("🥐", end=" ")
            elif s.type == "move":
                print("🚚", end=" ")
            elif s.type == "qcurve":
                print("🥨", end=" ")
        print("|", end=" ")
        counter += 1

    print("")
