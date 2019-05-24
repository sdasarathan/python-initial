import os

# Read files from windows operating system
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("\\", "\\\\")
# print(dir_path)
fileName = dir_path + '\\sample.txt'
with open(fileName, mode='r') as myFile:
    contents = myFile.read()

# append changes to the file
with open(fileName, mode='a') as myFile:
    myFile.write("Adding Changes")
print(contents)
