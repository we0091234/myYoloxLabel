import os
import shutil

def allFilePath(rootPath,allFIleList):
    fileList = os.listdir(rootPath)
    for temp in fileList:
        if os.path.isfile(os.path.join(rootPath,temp)):
            allFIleList.append(os.path.join(rootPath,temp))
        else:
            allFilePath(os.path.join(rootPath,temp),allFIleList)

fileFolder = r"/home/xiaolei/train_data/yolov3-channel-and-layer-pruning-master/data/dataHz/val"
# fileFolder = r"/home/xiaolei/train_data/HarzoneData/trianRar/"
saveFolder = r"/home/xiaolei/train_data/HarzoneData/MyVocFormat/val"

fileList =[]

allFilePath(fileFolder,fileList)
ic=70000
for file in fileList:
    if file.endswith(".jpg"):
        jpgPath = file
        txtPath = file.replace(".jpg",".txt")
        if os.path.exists(txtPath) and os.path.exists(file):
            ic+=1
            index =str(ic).zfill(6)
            newPicName=index+".jpg"
            newPicPath = os.path.join(saveFolder,newPicName)
            newTxtPath = newPicPath.replace(".jpg",".txt")
            # print(file,newPicPath)
            # print(txtPath,newTxtPath)
            print(ic,file)
            shutil.copy(file,newPicPath)
            shutil.copy(txtPath,newTxtPath)


print("{} pic done".format(ic) )

