from vanilla.dialogs import *
import metricsMachine
font = metricsMachine.CurrentFont()

print(font)

selectedFile = getFile("Select file to import", allowsMultipleSelection=False, fileTypes=["ufo"])

print(selectedFile)

font.kerning.importKerning(selectedFile[0])