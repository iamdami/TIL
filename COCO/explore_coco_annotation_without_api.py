import json, cv2
# import time

jsonPath = "../cocoToYoloFormat/annotations/instances_train2017.json"

with open(jsonPath, 'r') as f:
    fReadInstance = f.read()

loadJson = json.loads(fReadInstance)
# print(len(loadJson['annotations']))

for anno in loadJson['annotations']:
    bboxPt = anno['bbox']

    float_minX, float_minY, float_width, float_height = anno['bbox']
    minX = int(float_minX)
    minY = int(float_minY)
    width= int(float_width)
    height = int(float_height)
    # print(minX, minY, width, height)

    maxX = minX + width    
    maxY = minY + height    
    # print(maxX, maxY)

    imgName = f"{str(anno['image_id']).zfill(12)}.jpg"
    readImg = cv2.imread(f"train2017/{imgName}")
    h, w, c = readImg.shape
    # print(h, w)

    centerX = ((minX+maxX)/2)/w 
    centerY = ((minY+maxY)/2)/h
    centerW = (abs(minX-maxX)/2)/w
    centerH = (abs(minX+maxX)/2)/h
    # print(centerX, centerY, centerW, centerH)

    bboxPt = [centerX, centerY, centerW, centerH]

    txtFileName = f"{str(anno['image_id']).zfill(12)}.txt"

    catID = anno['category_id']
    labelPt = " ".join(list(map(str, bboxPt)))

    writeTxt = f"{catID} {labelPt}"

    print(f"text File Name: {txtFileName}")
    print(f"text: {writeTxt}")

    with open(f"trainLabel/{txtFileName}", 'a') as f:
        f.write(f"{writeTxt}\n")

    # time.sleep(20)
