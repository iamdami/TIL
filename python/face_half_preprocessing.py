import os, cv2

dataRoot = "../face/augmentation/"
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
        cv2.imwrite("asd.jpg", cropImg)
        break
    break
