# make tests of specific subsets using fontTools.instancer

import sys
import subprocess
import os
import shutil


VF = sys.argv[1]
outputDir = "font_betas/font_subset_tests"
subprocess.check_call(f'mkdir -p {outputDir}'.split())

# keys are file names; values are options for subsetter
testSubsets = {
    "wght_300_800": "wght=300:800 CASL=0 MONO=0 slnt=0 ital=0.5",
    "wght_300_1000": "wght=300:1000 CASL=0 MONO=0 slnt=0 ital=0.5",
    "CASL_0_1": "CASL=0:1 wght=400 MONO=0 slnt=0 ital=0",
    "MONO_0_1": "MONO=0:1 wght=400 CASL=0 slnt=0 ital=0",
    "wght_300_800-slnt0_15": "wght=300:800 slnt=-15:0 MONO=0 CASL=0",
    "wght_300_800-slnt0_15-ital_05": "wght=300:800 slnt=-15:0 ital=0.5 MONO=0 CASL=0 "
}


existingFiles = []

for dir in os.walk(outputDir):
    for file in dir[2]:
        existingFiles.append(file)

for key in testSubsets.keys():
    fileToMake = f"recursive--{key}.ttf"
    if fileToMake not in existingFiles:
        command = f"fonttools varLib.instancer {VF} {testSubsets[key]} -o {outputDir}/recursive--{key}.ttf"
        subprocess.check_call(command.split())
        print("\n-------------------------------\n")

# go through output directory to convert to woff2
subprocess.check_call(f'mkdir -p {outputDir}/woff2'.split())
for dir in os.walk(outputDir):
    for file in dir[2]:
        if "woff2" not in file:
            subprocess.check_call(f"woff2_compress {dir[0]}/{file}".split())
            shutil.move(f"{dir[0]}/{file.replace('.ttf','.woff2')}",f"{dir[0]}/woff2/{file.replace('.ttf','.woff2')}")