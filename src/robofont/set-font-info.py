from vanilla.dialogs import *

inputFonts = getFile("select UFOs", allowsMultipleSelection=True, fileTypes=["ufo"])

for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)
    
    # for other font info attributes, see 
    # http://unifiedfontobject.org/versions/ufo3/fontinfo.plist/
    
    f.info.openTypeOS2VendorID = "ARRW"    
    
    f.save()
    f.close()