from vanilla.dialogs import *
import metricsMachine
from mojo.UI import OutputWindow

copyFrom = getFile("Select file to copy from", allowsMultipleSelection=False, fileTypes=["ufo"])[0]
importTo = getFile("Select files to copy to", allowsMultipleSelection=True, fileTypes=["ufo"])

OutputWindow().show()
OutputWindow().clear()

fontToCopyFrom = OpenFont(copyFrom, showInterface=False)

copyFrom = metricsMachine.MetricsMachineFont(fontToCopyFrom.naked())

for fontPath in importTo:
    if fontPath != copyFrom:
        print(fontPath)

        fontToOpen = OpenFont(fontPath, showInterface=False)
        print(fontToOpen)
        
        copyTo = metricsMachine.MetricsMachineFont(fontToOpen.naked())
        copyTo.kerning.importKerning(copyFrom)
        
        fontToOpen.save()
        fontToOpen.close()


# alternative: maybe this could instead export a feature file, and the others would just read that?