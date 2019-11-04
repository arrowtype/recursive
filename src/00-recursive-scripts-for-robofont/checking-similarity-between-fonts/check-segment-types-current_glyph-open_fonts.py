from mojo.UI import OutputWindow

g = CurrentGlyph()

OutputWindow().clear()
OutputWindow().show()

firstColWidth = 20

print("")
print("FONT".ljust(firstColWidth + 1), end=" ")
print("|", end=" ")

key = "| 🥐 = curve | 📏 = line | 🚚 = move | 🥨 = qcurve"
print(f"Contours & segments in /{g.name} {key}")

print("".ljust(firstColWidth + 1, "-") + " | " + "".ljust(96, "-"))

for i, f in enumerate(AllFonts()):
    print(f.info.styleName.ljust(firstColWidth + 1), end=" ")
    print("|", end=" ")
    for c in f[g.name]:
        print(f"C{str(i).rjust(2, '0')}", end=" ")
        print(f"[{len(c.segments)}]", end=" ")
        for s in c:
            if s.type == "line":
                print("📏", end=" ")
            elif s.type == "curve":
                print("🥐", end=" ")
            elif s.type == "move":
                print("🚚", end=" ")
            elif s.type == "qcurve":
                print("🥨", end=" ")
        print("|", end=" ")
    print("")
    