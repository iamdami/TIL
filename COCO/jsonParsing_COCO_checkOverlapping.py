import json, cv2
import os

jsonPath = "../coco_dataset/annotations/instances_train2017.json"

with open(jsonPath, 'r') as f:
    readJson = f.read()

loadJson = json.loads(readJson)
catIDList = [8]  # truck

for idx, anno in enumerate(loadJson['annotations']):
    catID = anno['category_id']  # category ID
    bboxPT = anno['bbox']  # coordinate of bbox
    imgID = anno['image_id']  # image name
    if catID in catIDList:
        imgName = f"{str(imgID).zfill(12)}.jpg"
        readImg = cv2.imread(f"../coco_dataset/images/train2017/{imgName}")
        h, w, c = readImg.shape
        # if h > 640 or w > 640:
        #     print("over size")
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
        writeTxt = f"2 {labelPT}"

        print(f"Text File Name: {txtFileName}")
        print(f"Text: {writeTxt}")

        # check if the file overlapped or not
        if not os.path.exists(f"truck_images/{imgName}"):
            cv2.imwrite(f"truck_images/{imgName}", readImg)

        with open(f"truck_labels/{txtFileName}", 'a') as f:
            f.write(f"{writeTxt}\n")
            
    # percentage bar
    # if idx % 1000 == 0:
    #     print(f"percent : {idx/len(loadJson['annotations'])*100}%")
