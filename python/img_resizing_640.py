import cv2, os

data_root_path = ""
imgDataFolderNameList = ["images/train", "images/val"]
labelDataFolderNameList = ["labels/train", "labels/val"]

for i, imgDataFolderName in enumerate(imgDataFolderNameList):
    imgDataFolderPath = os.path.join(data_root_path, imgDataFolderName)
    imgNameList = os.listdir(imgDataFolderPath)

    for imgName in imgNameList:
        imgPath = os.path.join(imgDataFolderPath, imgName)
        dataName = imgName.split(".")[0]
        txtFilePath = os.path.join(data_root_path, labelDataFolderNameList[i], dataName + ".txt")
        img = cv2.imread(imgPath)
        ori_h, ori_w, c = img.shape
        if ori_h > ori_w:
            h = 640
            w = int(ori_w * h / ori_h)
        elif ori_h < ori_w:
            w = 640
            h = int(ori_h * w / ori_w)
        else:
            h = 640
            w = 640

        img = cv2.resize(img, (w, h))
        cv2.imwrite(f"images_car_plate/{imgName}", img)
