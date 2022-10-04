import json, cv2
import os, torch
from models.common import DetectMultiBackend
from utils.general import (check_img_size, non_max_suppression, scale_coords)
from utils.dataloaders import LoadImages

jsonPath = "/coco_dataset/annotations/instances_train2017.json"
weights = "/yolov5/ptFiles/yolov5s6Plate.pt"  # plate pt file

with open(jsonPath, 'r') as f:
    readJson = f.read()

loadJson = json.loads(readJson)
catIDList = [1, 3, 6, 8]  # truck

model = DetectMultiBackend(weights, device = torch.device("cuda:0"))
stride, names, pt = model.stride, model.names, model.pt
imgsz = check_img_size((640, 640), s = stride)

for idx, anno in enumerate(loadJson['annotations']):
    catID = anno['category_id']  # category ID
    bboxPT = anno['bbox']  # coordinate of bbox
    imgID = anno['image_id']  # image name
    if catID in catIDList:
        imgName = f"{str(imgID).zfill(12)}.jpg"
        readImg = cv2.imread(f"/coco_dataset/images/train2017/{imgName}")

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
        if catID == 1:
            writeTxt = f"0 {labelPT}" 
        elif catID == 3:
            writeTxt = f"1 {labelPT}" 
        elif catID == 6:
            writeTxt = f"2 {labelPT}" 
        elif catID == 8:
            writeTxt = f"3 {labelPT}" 

        print(f"Text File Name: {txtFileName}")
        print(f"Text: {writeTxt}")

        # check if the file overlapped or not
        if not os.path.exists(f"4labels_coco_imgs/{imgName}"):
            cv2.imwrite(f"4labels_coco_imgs/{imgName}", readImg)

        with open(f"4labels_coco_labels/{txtFileName}", 'a') as f:
            f.write(f"{writeTxt}\n")

labels_txt_file_name_list = os.listdir("4labels_coco_labels")

for labels_txt_file_name in labels_txt_file_name_list:
    txt_path = os.path.join("4labels_coco_labels", labels_txt_file_name)
    with open(txt_path, 'r') as f:
        txt_list = f.readlines()
        cat_id = list()
        for txt in txt_list:
            txt = txt.split(' ')
            cat_id.append(int(txt[0]))
        cat_id = list(set(cat_id))
    if len(cat_id) == 1 and 0 in cat_id:
        # skip plate detection
        continue
    else:
        # detect plate
        imgName = labels_txt_file_name.replace(".txt", "jpg")
        img_path = os.path.join("4labels_coco_imgs", imgName)
        dataset = LoadImages(img_path, img_size = imgsz, stride = stride, auto = pt)

        for path, im, im0s,_,_ in dataset:
            im = torch.from_numpy(im).to(torch.device("cuda:0"))
            im = im.float()
            im /= 255
            if len(im.shape) == 3:
                im = im[None]
            
            pred = model(im, augment = False, visualize = False)
            pred = non_max_suppression(pred, 0.25, 0.45, None, False, max_det = 1000)

            for i, det in enumerate(pred):
                p, im0, frame = path, im0s.copy(), getattr(dataset, "frame", 0)

                if len(det):
                    det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()

                    for c in det[:, -1].unique():
                        for *xyxy, conf, cls in reversed(det):
                            xyxy = list(map(int, xyxy))
                            recImg = cv2.rectangle(im0, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (155, 0, 45), 2)
                            c_x = ((xyxy[0] + xyxy[2]) / 2) / w
                            c_y = ((xyxy[1] + xyxy[3]) / 2) / h
                            c_w = abs(xyxy[2] - xyxy[0]) / w
                            c_h = abs(xyxy[3] - xyxy[1]) / h

                            bboxPT = [c_x, c_y, c_w, c_h]
                            labelPT = " ".join(list(map(str, bboxPT)))
                            writeTxt = f"4 {labelPT}" # plate
                            print(f"Plate label Appended Text File Name: {txtFileName}")
                            print(f"Appended Text: {writeTxt}")
                            
                            # Append plate label
                            with open(txt_path, 'a') as f:
                                f.write(f"{writeTxt}\n")
