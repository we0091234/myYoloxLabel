import os
import shutil

def allFilePath(rootPath,allFIleList):
    fileList = os.listdir(rootPath)
    for temp in fileList:
        if os.path.isfile(os.path.join(rootPath,temp)):
            allFIleList.append(os.path.join(rootPath,temp))
        else:
            allFilePath(os.path.join(rootPath,temp),allFIleList)

fileFolder = r"/home/xiaolei/ramdisk/VOCdevkit/VOC2007/Annotations/"
# fileFolder = r"/home/xiaolei/train_data/HarzoneData/trianRar/"
saveFolder = r"/home/xiaolei/train_data/HarzoneData/testMv"

fileList =[]

allFilePath(fileFolder,fileList)
ic=0
for file in fileList:
    if file.endswith(".xml"):
        if  os.path.getsize(file):
            ic+=1
            print(file)


print("{} pic done".format(ic) )