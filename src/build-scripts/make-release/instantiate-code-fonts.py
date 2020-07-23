"""
    A script to generate Recursive fonts for code with:
    - An abbreviated family name to avoid macOS style-linking bug
        - Rec Mono
    - A reduced italic slant (probably -10 degrees)
    - The following static instances:
        - Linear
        - Linear Italic
        - Linear Bold
        - Linear Bold Italic
        - Casual
        - Casual Italic
        - Casual Bold
        - Casual Bold Italic

    USAGE:

    python <path>/instantiate-code-fonts.py <recursive-VF>

    NOTE: assumes it will act on the Recursive variable font as of e84015de.
"""

import os
import pathlib
from fontTools import ttLib
from fontTools.varLib import instancer
from opentype_feature_freezer import cli as pyftfeatfreeze
import subprocess
import shutil
import fire
from dlig2calt import dlig2calt

# instances to split

instanceValues = {
    # # Linear package
    # "Linear": {
    #     "Linear": {
    #         "MONO": 1,
    #         "CASL": 0,
    #         "wght": 400,
    #         "slnt": 0,
    #         "CRSV": 0,
    #         "style": "Regular",
    #     },
    #     "Linear Italic": {
    #         "MONO": 1,
    #         "CASL": 0,
    #         "wght": 400,
    #         "slnt": -10,
    #         "CRSV": 1,
    #         "style": "Italic",
    #     },
    #     "Linear Bold": {
    #         "MONO": 1,
    #         "CASL": 0,
    #         "wght": 700,
    #         "slnt": 0,
    #         "CRSV": 0,
    #         "style": "Bold",
    #     },
    #     "Linear Bold Italic": {
    #         "MONO": 1,
    #         "CASL": 0,
    #         "wght": 700,
    #         "slnt": -10,
    #         "CRSV": 1,
    #         "style": "Bold Italic",
    #     },
    # },
    # # Casual package
    # "Casual": {
    #     "Casual": {
    #         "MONO": 1,
    #         "CASL": 1,
    #         "wght": 400,
    #         "slnt": 0,
    #         "CRSV": 0,
    #         "style": "Regular",
    #     },
    #     "Casual Italic": {
    #         "MONO": 1,
    #         "CASL": 1,
    #         "wght": 400,
    #         "slnt": -10,
    #         "CRSV": 1,
    #         "style": "Italic",
    #     },
    #     "Casual Bold": {
    #         "MONO": 1,
    #         "CASL": 1,
    #         "wght": 700,
    #         "slnt": 0,
    #         "CRSV": 0,
    #         "style": "Bold",
    #     },
    #     "Casual Bold Italic": {
    #         "MONO": 1,
    #         "CASL": 1,
    #         "wght": 700,
    #         "slnt": -10,
    #         "CRSV": 1,
    #         "style": "Bold Italic",
    #     },
    # },
    # SemiCasual package
    "SemiCasual": {
        "SemiCasual": {
            "MONO": 1,
            "CASL": 0.5,
            "wght": 400,
            "slnt": 0,
            "CRSV": 0,
            "style": "Regular",
        },
        # "SemiCasual Italic": {
        #     "MONO": 1,
        #     "CASL": 0.5,
        #     "wght": 400,
        #     "slnt": -10,
        #     "CRSV": 1,
        #     "style": "Italic",
        # },
        # "SemiCasual Bold": {
        #     "MONO": 1,
        #     "CASL": 0.5,
        #     "wght": 700,
        #     "slnt": 0,
        #     "CRSV": 0,
        #     "style": "Bold",
        # },
        # "SemiCasual Bold Italic": {
        #     "MONO": 1,
        #     "CASL": 0.5,
        #     "wght": 700,
        #     "slnt": -10,
        #     "CRSV": 1,
        #     "style": "Bold Italic",
        # },
    },
    # # Duotone package
    # "Duotone": {
    #     "Duotone": {
    #         "MONO": 1,
    #         "CASL": 0,
    #         "wght": 400,
    #         "slnt": 0,
    #         "CRSV": 0,
    #         "style": "Regular",
    #     },
    #     "Duotone Italic": {
    #         "MONO": 1,
    #         "CASL": 1,
    #         "wght": 400,
    #         "slnt": -10,
    #         "CRSV": 1,
    #         "style": "Italic",
    #     },
    #     "Duotone Bold": {
    #         "MONO": 1,
    #         "CASL": 0,
    #         "wght": 700,
    #         "slnt": 0,
    #         "CRSV": 0,
    #         "style": "Bold",
    #     },
    #     "Duotone Bold Italic": {
    #         "MONO": 1,
    #         "CASL": 1,
    #         "wght": 700,
    #         "slnt": -10,
    #         "CRSV": 1,
    #         "style": "Bold Italic",
    #     },
    # },
}

# GET / SET NAME HELPER FUNCTIONS


def getFontNameID(font, ID, platformID=3, platEncID=1):
    name = str(font["name"].getName(ID, platformID, platEncID))
    return name


def setFontNameID(font, ID, newName):

    print(f"\n\t• name {ID}:")
    macIDs = {"platformID": 3, "platEncID": 1, "langID": 0x409}
    winIDs = {"platformID": 1, "platEncID": 0, "langID": 0x0}

    oldMacName = font["name"].getName(ID, *macIDs.values())
    oldWinName = font["name"].getName(ID, *winIDs.values())

    if oldMacName != newName:
        print(f"\n\t\t Mac name was '{oldMacName}'")
        font["name"].setName(newName, ID, *macIDs.values())
        print(f"\n\t\t Mac name now '{newName}'")

    if oldWinName != newName:
        print(f"\n\t\t Win name was '{oldWinName}'")
        font["name"].setName(newName, ID, *winIDs.values())
        print(f"\n\t\t Win name now '{newName}'")


# ----------------------------------------------
# MAIN FUNCTION

oldName = "Recursive"


def splitFont(
        fontPath,
        outputDirectory="fonts/rec_mono-for-code",
        newName="Rec Mono",
        ttc=False,
        zip=False,
):

    # access font as TTFont object
    varfont = ttLib.TTFont(fontPath)

    fontFileName = os.path.basename(fontPath)

    for package in instanceValues:
        outputSubDir = f"{outputDirectory}/{package}"

        for instance in instanceValues[package]:

            print(instance)

            instanceFont = instancer.instantiateVariableFont(
                varfont,
                {
                    "wght": instanceValues[package][instance]["wght"],
                    "CASL": instanceValues[package][instance]["CASL"],
                    "MONO": instanceValues[package][instance]["MONO"],
                    "slnt": instanceValues[package][instance]["slnt"],
                    "CRSV": instanceValues[package][instance]["CRSV"],
                },
            )

            # UPDATE NAME ID 6, postscript name
            currentPsName = getFontNameID(instanceFont, 6)
            newPsName = (currentPsName.replace("Sans", "").replace(
                oldName,
                newName.replace(" ", "")).replace("LinearLight",
                                                  instance.replace(" ", "")))
            setFontNameID(instanceFont, 6, newPsName)

            # UPDATE NAME ID 4, full font name
            currentFullName = getFontNameID(instanceFont, 4)
            newFullName = (currentFullName.replace("Sans", "").replace(
                oldName, newName).replace(" Linear Light", instance))
            setFontNameID(instanceFont, 4, newFullName)

            # UPDATE NAME ID 3, unique font ID
            currentUniqueName = getFontNameID(instanceFont, 3)
            newUniqueName = (currentUniqueName.replace("Sans", "").replace(
                oldName,
                newName.replace(" ", "")).replace("LinearLight",
                                                  instance.replace(" ", "")))
            setFontNameID(instanceFont, 3, newUniqueName)

            # ADD name 2, style linking name
            newStyleLinkingName = instanceValues[package][instance]["style"]
            setFontNameID(instanceFont, 2, newStyleLinkingName)
            setFontNameID(instanceFont, 17, newStyleLinkingName)

            # UPDATE NAME ID 1, unique font ID
            currentFamName = getFontNameID(instanceFont, 1)
            newFamName = (currentFamName.replace(" Sans", "").replace(oldName, newName).replace(
                "Linear Light",
                instance.replace(" " + instanceValues[package][instance]["style"], ""),
            ))
            setFontNameID(instanceFont, 1, newFamName)
            setFontNameID(instanceFont, 16, newFamName)

            newFileName = fontFileName.replace(oldName, newName.replace(
                " ", "")).replace("_VF_",
                                  "-" + instance.replace(" ", "") + "-")

            # make dir for new fonts
            pathlib.Path(outputSubDir).mkdir(parents=True, exist_ok=True)

            # drop STAT table to allow RIBBI style naming & linking on Windows
            del instanceFont["STAT"]

            outputPath = f"{outputSubDir}/{newFileName}"

            # save font
            instanceFont.save(outputPath)

            # freeze in rvrn features with pyftfeatfreeze
            # pyftfeatfreeze.main(["--features=rvrn", outputPath, outputPath])

            # swap dlig2calt to make code ligatures work in old code editor apps
            dlig2calt(outputPath, inplace=True)

        # -----------------------------------------------------------
        # make TTC (truetype collection) of fonts – doesn't currently work on Mac very well :(

        if ttc:
            # make list of fonts in subdir
            fontPaths = [
                os.path.abspath(outputSubDir + "/" + x)
                for x in os.listdir(outputSubDir)
            ]

            # form command
            command = f"otf2otc {' '.join(fontPaths)} -o {outputDirectory}/RecMono-{package}.ttc"
            print("▶", command, "\n")

            # run command in shell
            subprocess.run(command.split(), check=True, text=True)

            # remove dir with individual fontpaths
            shutil.rmtree(os.path.abspath(outputSubDir))

    # Make zip of output, then put inside output directory
    if zip:
        shutil.make_archive(f"{outputDirectory}", "zip", outputDirectory)
        shutil.move(
            f"{outputDirectory}.zip",
            f"{outputDirectory}/{outputDirectory.split('/')[-1]}.zip",
        )


if __name__ == "__main__":
    fire.Fire(splitFont)
