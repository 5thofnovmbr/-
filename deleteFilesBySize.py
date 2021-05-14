import os
import shutil

currentDir = "./"

minFileSize=float(input("Minimum size of file(MB): "))
dirPath =f"./under {minFileSize}MB/"

fileList = os.listdir(currentDir)

if not os.path.isdir(dirPath):
    os.mkdir(dirPath)

for file in fileList:

    fileSize = os.path.getsize(currentDir+file)
    if (fileSize < (minFileSize*1024*1014)) and (file[-3:] != ".py"):
        shutil.move(currentDir+file, dirPath+file)
        print(file)
