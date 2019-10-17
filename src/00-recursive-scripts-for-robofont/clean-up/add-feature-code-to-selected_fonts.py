from vanilla.dialogs import *


# featureFile="../../features/features.fea"
featureFile = getFile("select OpenType feature file", allowsMultipleSelection=False, fileTypes=["fea"])

print(featureFile)

with open(featureFile[0], "r") as f:
    feaText = f.read()
    print(feaText)

def addFeatureCode(f):
    f.features.text = feaText
    
inputFonts = getFile("select masters to add feature code to", allowsMultipleSelection=True, fileTypes=["ufo"])
    
for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)

    f.features.text = feaText

    fontName = f.info.familyName + " " + f.info.styleName
    print("feature code added to " + fontName)
    f.save()
    f.close()