import json,cv2
jsonPath = "annotations/instances_train2017.json"
with open(jsonPath,"r") as f:
    fileReadInstance = f.read()
valjson = json.loads(fileReadInstance)
print(len(valjson['annotations']))
for valAnno in valjson['annotations']:
    # image의 box좌표정보
    boxPT = valAnno['bbox']
    
    ######################
    float_xCenter,float_yCenter,float_width,float_height = valAnno['bbox']
    minX = int(float_xCenter)
    minY = int(float_yCenter)
    width = int(float_width)
    height = int(float_height)

    # print(minX, minY, width, height)

    maxX = minX + width
    maxY = minY + height

    # print(maxX, maxY)
    imgName = f"{str(valAnno['image_id']).zfill(12)}.jpg"
    img = cv2.imread(f"train2017/{imgName}")
    h,w,c = img.shape
    print(h,w)
    x1,y1,cw,ch = ((minX+maxX)/2)/w,((minY+maxY)/2)/h,(abs(minX-maxX))/w,(abs(minY-maxY))/h
    print(x1,y1,cw,ch)
    boxPT = [x1,y1,cw,ch]
    # recImg = cv2.rectangle(img, (minX, minY), (maxX, maxY), (255, 0, 0), 3)
    # cv2.imwrite("./recImg.jpg", recImg)
    # break
    ######################

    # 레이블 정보
    categoryID = valAnno['category_id']
    ptLabel = ' '.join(list(map(str,boxPT)))
    # txt파일로 write 할 내용
    writeText = f"{categoryID} {ptLabel}"
    textFlieName = f"{str(valAnno['image_id']).zfill(12)}.txt"

    print(f"txtFileName : {textFlieName}")
    print(f"txtFileText : {writeText}")
    with open(f"train_label/{textFlieName}",'a') as f:
        f.write(f"{writeText}\n")
