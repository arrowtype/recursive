# import os

# dir_path = os.path.dirname(os.path.realpath(__file__))

# print(dir_path)

folderToGet = "../../../../Users/stephennixon/Environments/gfonts3/lib/python3.6"

# codeExample= ""

# # for file in folder
# for filename in os.listdir(folderToGet):
#     if filename.endswith(".py"): 
#         # print(os.path.join(directory, filename))
#         file_object = open(folderToGet + "/" + filename, 'r')
#         codeExample += file_object.read()
#         # print(filename)

# print(codeExample)

from pathlib import Path

pathlist = Path(folderToGet).glob('**/*.py')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)

    # open file
    # add contents to loooong variable