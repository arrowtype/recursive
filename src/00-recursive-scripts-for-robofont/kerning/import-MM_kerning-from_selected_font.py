from vanilla.dialogs import *
import metricsMachine
from mojo.UI import OutputWindow

copyFrom = getFile("Select file to copy from", allowsMultipleSelection=False, fileTypes=["ufo"])[0]
importTo = getFile("Select files to copy to", allowsMultipleSelection=True, fileTypes=["ufo"])


OutputWindow().show()
OutputWindow().clear()

# maybe this could instead export a feature file, and the others would just read that?

for fontPath in importTo:
    if fontPath != copyFrom:
        print(fontPath)

        fontToOpen = OpenFont(fontPath, showInterface=False)
        
        
        print(fontToOpen)
        
        font = metricsMachine.CurrentFont()
        font.kerning.importKerning(copyFrom)
        print(CurrentFont())
        
        fontToOpen.save()
        fontToOpen.close()

