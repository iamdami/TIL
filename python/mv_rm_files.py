import os, shutil

imgRTPath = "Training/oriData"
jsonRTPath = "Training/labelData"

imgCatFolderList = os.listdir(imgRTPath)
jsonCatFolderList = os.listdir(jsonRTPath)

# for img
# for imgCatFolder in imgCatFolderList:
#     imgNameList = os.listdir(os.path.join(imgRTPath, imgCatFolder))
#     for imgName in imgNameList:
#         imgFullPath = os.path.join(imgRTPath, imgCatFolder, imgName)
#         shutil.move(imgFullPath, imgRTPath)
#     os.rmdir(os.path.join(imgRTPath, imgCatFolder))

# for json
for jsonCatFolder in jsonCatFolderList:
    jsonNameList = os.listdir(os.path.join(jsonRTPath, jsonCatFolder))
    for jsonName in jsonNameList:
        jsonFullPath = os.path.join(jsonRTPath, jsonCatFolder, jsonName)
        shutil.move(jsonFullPath, jsonRTPath)
    os.rmdir(os.path.join(jsonRTPath, jsonCatFolder))
