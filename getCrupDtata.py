import cv2
import os


def allFilePath(rootPath,allFIleList):
    fileList = os.listdir(rootPath)
    for temp in fileList:
        if os.path.isfile(os.path.join(rootPath,temp)):
            allFIleList.append(os.path.join(rootPath,temp))
        else:
            allFilePath(os.path.join(rootPath,temp),allFIleList)


filePath = r"/home/xiaolei/train_data/HarzoneData/MyVocFormat/VOCdevkit/VOC2007/JPEGImages"

fileList =[]
allFilePath(filePath,fileList)
i=0
for picPath in fileList:
    img = cv2.imread(filePath)
    i+=1
    print(i,picPath)

