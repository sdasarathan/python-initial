import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("\\", "\\\\")
# print(dir_path)
with open(dir_path + '\\sample.txt') as myFile:
    contents = myFile.read()
print(contents)
