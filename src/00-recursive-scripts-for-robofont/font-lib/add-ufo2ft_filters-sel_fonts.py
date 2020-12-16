from vanilla.dialogs import *

inputFonts = getFile("select UFOs", allowsMultipleSelection=True, fileTypes=["ufo"])

for fontPath in inputFonts:
    font = OpenFont(fontPath, showInterface=False)

    # for other font info attributes, see
    # http://unifiedfontobject.org/versions/ufo3/fontinfo.plist/

    # un-nest nested components # https://github.com/googlefonts/fontbakery/issues/296
    font.lib["com.github.googlei18n.ufo2ft.filters"] = [
            {
                'name': 'decomposeComponents', 
                'include': "Eth".split()
            },
            {
                'name': 'decomposeTransformedComponents', 
                'pre': 1
            },
            {
                'name': 'flattenComponents', 
                'pre': 1
            },
    ]

    print("Updated info for:")
    print("family: ", font.info.familyName, "\n ", "style: ", font.info.styleName)

    font.save()
    font.close()