glyphsWithSupportLayer = "w"

fontsToCheck = []

for f in AllFonts():
    for layer in f.layers:
        if layer.name == "support.w.middle":
            fontsToCheck.append(f)
            
print("Glyphs that shouldn't be in layer `support.w.middle`:")

for f in fontsToCheck:
    print("\n",f.info.styleName)
    for layer in f.layers:
        if layer.name == "support.w.middle":
            for glyphName in layer.keys():
                if glyphName not in glyphsWithSupportLayer.split(" "):
                    print("  •", glyphName)
                    # del layer[glyphName] # NOT WORKING YET
