# from os import walk

# imgPath = "./val2017"
# labelpath = "./label"

# imgRes = []
# labelRes = []

# for (dirPath, dirName, fileName) in walk(imgPath):
#     imgRes.extend(fileName)
#     rmv_imgRes = ".jpg"
#     imgRes = [elem.replace(rmv_imgRes, "") for elem in imgRes]

# for (dirPath, dirName, fileName) in walk(labelpath):
#     labelRes.extend(fileName)
#     rmv_labelRes = ".txt"
#     labelRes = [elem.replace(rmv_labelRes, "") for elem in labelRes]

# # print(imgRes)
# # print(labelRes)

# if (imgRes != labelRes):
#     notInImgRes = [elem for elem in imgRes if elem not in labelRes]
#     notInLabelRes = [elem for elem in labelRes if elem not in imgRes]
#     print(len(notInImgRes))
#     print(notInLabelRes)
    
# else:
#     pass




import os
imgPath = "./train2017"
labelpath = "./train_label"
imgList = os.listdir(imgPath)
labelList = os.listdir(labelpath)
print(len(imgList))
print(len(labelList))

delNameList = list()
if len(labelList) < len(imgList):
    for imgName in imgList:
        delNameList.append(imgName.split('.')[0])
    for labelName in labelList:
        delNameList.remove(labelName.split('.')[0])
    print(f"1: {delNameList}")
elif len(labelList) > len(imgList):
    for labelName in labelList:
        delNameList.remove(labelName.split('.')[0])
    print(f"2: {delNameList}")
    for imgName in imgList:
        delNameList.append(imgName.split('.')[0])
else:
    print("Equal")
    exit()
for i,delName in enumerate(delNameList):
    delName = f"{delName}.jpg"
    os.system(f"rm -rf {os.path.join(imgPath,delName)}")

print(len(imgList))
print(len(labelList))
