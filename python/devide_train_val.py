import os, random, shutil

imgFolderNamePath = "images"
valImgFolderNamePath = "img_val"
labelFolderNamePath = "labels"
valLabelFolderNamePath = "label_val"

imageNameList = os.listdir(imgFolderNamePath)

sampleImgNameList = random.sample(imageNameList, int(len(imageNameList) * 0.2))
for sampleImgName in sampleImgNameList:
    valImgPath = os.path.join(imgFolderNamePath, sampleImgName)
    shutil.move(valImgPath, valImgFolderNamePath)

    valLabelName = sampleImgName.split(".")[0] + ".txt"
    valLabelPath = os.path.join(labelFolderNamePath, valLabelName)
    shutil.move(valLabelPath, valLabelFolderNamePath)
