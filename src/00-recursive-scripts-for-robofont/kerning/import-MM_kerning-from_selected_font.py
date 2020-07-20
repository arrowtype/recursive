from vanilla.dialogs import *
import metricsMachine
from mojo.UI import OutputWindow

## use if you want to select different files
copyFrom = getFile("Select file to copy from", allowsMultipleSelection=False, fileTypes=["ufo"])[0]
importTo = getFile("Select files to copy to", allowsMultipleSelection=True, fileTypes=["ufo"])
print(copyFrom)
print(importTo)

## use if you wish to just make this a one-button copy (update as needed)
# copyFrom = "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Casual B.ufo"
# importTo = (
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Casual A Slanted.ufo",
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Casual A.ufo",
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Casual B Slanted.ufo",
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Casual B.ufo",
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Casual C Slanted.ufo",
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Casual C.ufo",
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Linear A Slanted.ufo",
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Linear A.ufo",
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Linear B Slanted.ufo",
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Linear B.ufo",
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Linear C Slanted.ufo",
#     "/Users/stephennixon/type-repos/recursive/src/ufo/sans/Recursive Sans-Linear C.ufo"
# )

## uncomment if you wish to see output window
# OutputWindow().show()
# OutputWindow().clear()

for fontPath in importTo:
    if fontPath != copyFrom:
        print(f'Copying kerning from {copyFrom.split("/")[-1]} to {fontPath.split("/")[-1]}')

        fontToOpen = OpenFont(fontPath, showInterface=False)
        
        copyTo = metricsMachine.MetricsMachineFont(fontToOpen.naked(), showInterface=False)
        copyTo.kerning.importKerning(copyFrom)
        
        copyTo.save()
        copyTo.close()
        
        fontToOpen.close()


# alternative: maybe this could instead export a feature file, and the others would just read that?