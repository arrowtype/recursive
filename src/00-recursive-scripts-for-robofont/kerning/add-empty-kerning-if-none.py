from vanilla.dialogs import *
from mojo.UI import OutputWindow
import metricsMachine

## use if you want to select different files
files = getFile("Select file to copy from", allowsMultipleSelection=True, fileTypes=["ufo"])

## uncomment if you wish to see output window
OutputWindow().show()
OutputWindow().clear()

for fontPath in files:

    f = OpenFont(fontPath, showInterface=False)

    # groups = RKerning()

    # f.groups = groups

    print(len(f.groups))

    if len(f.kerning) == 0:
        f.kerning[("A", "A")] = 0
        del f.kerning[("A","A")]

    print(len(f.groups))

    f.save()
    f.close()


# common_keys_vals = [(key, [dict[key] for dict in components.keys()])]
