import os

def allFilePath(rootPath,allFIleList):
    fileList = os.listdir(rootPath)
    for temp in fileList:
        if os.path.isfile(os.path.join(rootPath,temp)):
            allFIleList.append(os.path.join(rootPath,temp))
        else:
            allFilePath(os.path.join(rootPath,temp),allFIleList)



filePath =r"/home/xiaolei/train_data/HarzoneData/MyVocFormat/val"
xmlpath=r"/home/xiaolei/train_data/HarzoneData/MyVocFormat/val"
txtFilePath =r"/home/xiaolei/train_data/HarzoneData/MyVocFormat/ImageSets/Main/test.txt"


jpgFileList = []

i=0

allFilePath(filePath,jpgFileList)
f = open(txtFilePath,"w")
for file in jpgFileList:
    if not file.endswith(".jpg"):
        continue
    fileName = file.split("/")[-1]
    xmlName = fileName.replace(".jpg",".xml")
    xmlfPath = os.path.join(xmlpath,xmlName)
    if os.path.exists(xmlfPath):
        fileNameNoHouzui = fileName.split(".")[0]
        i+=1
        f.write(fileNameNoHouzui+"\n")
        print(i,fileNameNoHouzui)
    else:
        print(file)

f.close()