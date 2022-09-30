# 얼굴 크롭이미지 얼굴 윗부분으로만 절반 잘라서 지정 폴더에 저장

import os, cv2

dataRoot = "../facekcl/augmentation/"
dataRootHalf = "../facekcl/augmentation_half/"
if not os.path.isdir(dataRootHalf):
    os.mkdir(dataRootHalf)
personIdxList = os.listdir(dataRoot)

for personIdx in personIdxList:
    personIdxPath = os.path.join(dataRoot, personIdx)
    imgNameList = os.listdir(personIdxPath)
    
    for imgName in imgNameList:
        imgFullPath = os.path.join(personIdxPath, imgName)
        imgRead = cv2.imread(imgFullPath)
        h, w, c = imgRead.shape
        half_h = int(h / 2)
        cropImg = imgRead[:half_h, :w]
        
        dataRootIdxHalf = os.path.join(dataRootHalf,personIdx)
        if not os.path.isdir(dataRootIdxHalf):
            os.mkdir(dataRootIdxHalf)
        cv2.imwrite(os.path.join(dataRootIdxHalf,imgName), cropImg)
