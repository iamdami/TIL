import json, cv2
import os

labelID = int(input("Enter COCO labelID: "))
categoryID = int(input("Enter categoryID: "))
dirName = str(input("Enter dirName: "))

jsonPath = "../coco_dataset/annotations/instances_train2017.json"

with open(jsonPath, 'r') as f:
    readJson = f.read()

loadJson = json.loads(readJson)
catIDList = [labelID]  # coco object category label id

for anno in loadJson['annotations']:
    catID = anno['category_id']
    bboxPT = anno['bbox']
    imgID = anno['image_id']
    if catID in catIDList:
        imgName = f"{str(imgID).zfill(12)}.jpg"
        readImg = cv2.imread(f"../coco_dataset/images/train2017/{imgName}")
        h, w, c = readImg.shape

        float_minX, float_minY, float_width, float_height = anno['bbox']
        minX = int(float_minX)
        minY = int(float_minY)
        width = int(float_width)
        height = int(float_height)
        
        # to YOLO bbox format
        maxX = minX + width
        maxY = minY + height

        centerX = ((minX+maxX)/2)/w
        centerY = ((minY+maxY)/2)/h
        centerW = width/w
        centerH = height/h

        bboxPT = [centerX, centerY, centerW, centerH]

        txtFileName = f"{str(imgID).zfill(12)}.txt"
        labelPT = " ".join(list(map(str, bboxPT)))
        writeTxt = f"{categoryID} {labelPT}"

        print(f"Text File Name: {txtFileName}")
        print(f"Text: {writeTxt}")
        
        # check if the file overlapped or not
        if not os.path.exists(f"{dirName}/{imgName}"):
            cv2.imwrite(f"{dirName}/{imgName}", readImg)

        with open(f"{dirName}/{txtFileName}", 'a') as f:
            f.write(f"{writeTxt}\n")
