import os


imgPath = "img/path/"
labelPath = "label/path"

imgNameList = os.listdir(imgPath)
labelNameList = os.listdir(labelPath)

imgNameOlnyList = list()
labelNameOnlyList = list()
rmNameList = list()

print(f"Ori imgNameList Num: {len(imgNameList)}")
print(f"Ori labelNameList Num: {len(labelNameList)}")
print("="*100)

# image Num is more bigger
if len(imgNameList) > len(labelNameList):
    print("image Num is more bigger")
    for imgName in imgNameList:
        imgNameOlnyList.append(imgName.split(".")[0])
    for labelName in labelNameList:
        labelNameOnlyList.append(labelName.split(".")[0])

    for i, imgName in enumerate(imgNameOlnyList):
        if imgName not in labelNameOnlyList:
            rmNameList.append(imgName)
    print(f"rmName Num: {len(rmNameList)}")
    print("-"*100)

    for i, rmName in enumerate(rmNameList):
        for imgName in imgNameList:
            if rmName in imgName:
                os.remove(os.path.join(imgPath, imgName))
                print(f"removed!: {os.path.join(imgPath, imgName)}")        
    print("-"*100)
    
    updatedImgNameList = os.listdir(imgPath)
    updatedLabelNameList = os.listdir(labelPath)
    print(f"Result imgNameList Num: {len(updatedImgNameList)}")
    print(f"Result labelNameList Num: {len(updatedLabelNameList)}")    
    exit()

# label Num is more bigger
elif len(imgNameList) < len(labelNameList):
    print("label Num is more bigger")
    for imgName in imgNameList:
        imgNameOlnyList.append(imgName.split(".")[0])
    for labelName in labelNameList:
        labelNameOnlyList.append(labelName.split(".")[0])
    for i, labelName in enumerate(labelNameOnlyList):
        if labelName not in imgNameOlnyList:
            rmNameList.append(labelName)
    print(f"rmName Num: {len(rmNameList)}")
    print("-"*100)

    for i, rmName in enumerate(rmNameList):
        for labelName in labelNameList:
            if rmName in labelName:
                os.remove(os.path.join(labelPath, labelName))
                print(f"removed!: {os.path.join(labelPath, labelName)}")
    print("-"*100)

    updatedImgNameList = os.listdir(imgPath)
    updatedLabelNameList = os.listdir(labelPath)
    print(f"Result imgNameList Num: {len(updatedImgNameList)}")
    print(f"Result labelNameList Num: {len(updatedLabelNameList)}")    
    exit()

# Equal
else:
    print("Equal!")
    exit() 
