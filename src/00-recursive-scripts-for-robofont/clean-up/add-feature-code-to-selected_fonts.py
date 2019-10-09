from vanilla.dialogs import *



inputFonts = getFile("select masters to add feature code to", allowsMultipleSelection=True, fileTypes=["ufo"])

featureFile="../../features/features.fea"

f=open(featureFile, "r")
if f.mode == 'r':
    feaText = f.read()
    print(feaText)

# feaText = """\
# include(../../features/features.fea);
# """ 



def addFeatureCode(f):
    f.features.text = feaText
    
    
for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)
    # addFeatureCode(f)

    f.features.text = feaText

    fontName = f.info.familyName + " " + f.info.styleName
    print("feature code added to " + fontName)
    f.save()
    f.close()