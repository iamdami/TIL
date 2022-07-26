import os
import numpy as np
from pathlib import Path
from xml.dom.minidom import parse
from shutil import copyfile

fileRT = "/home/ubuntu/dami/yolov5/lpdata/"
imgPath = f"{fileRT}images"
annoPath = f"{fileRT}annotations"

dataRT = "/home/ubuntu/dami/yolov5/lpDestDataset/"
destImgPath = f"{dataRT}train/images"
destLabelPath = f"{dataRT}train/labels"

files = os.listdir(annoPath)
# print(files)

def cordConverter(size, box):
    x1 = int(box[0])
    y1 = int(box[1])
    x2 = int(box[2])
    y2 = int(box[3])

    dw = np.float32(1. / int(size[0]))
    dh = np.float32(1. / int(size[1]))

    w = x2 - x1
    h = y2 - y1

    x = x1 + (w / 2)
    y = y1 + (h / 2)

    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh

    return [x, y, w, h]

def saveFile(imgFileName, size, imgBox):
    classes = ['plate']
    saveFileName = f"{destLabelPath}/{imgFileName}.txt"
    print(f"saveFileName: {saveFileName}")
    with open(saveFileName, "a") as filePath:
        for box in imgBox:
            cord = cordConverter(size, box[1:])
            cord.insert(0, 0)
            cord = list(map(str, cord))
            print(cord)
            filePath.write(f"{' '.join(cord)}\n")

def getXmlData(filePath, imgXmlFile):
    imgPath = f"{filePath}/{imgXmlFile}.xml"
    print(f"imgPath: {imgPath}")
    root = parse(imgPath)
    imgName = root.getElementsByTagName("fileName")
    imgSize = root.getElementsByTagName("size")[0]
    imgW = imgSize.getElementsByTagName("width")[0].childNodes[0].data
    imgH = imgSize.getElementsByTagName("height")[0].childNodes[0].data
    imgC = imgSize.getElementsByTagName("depth")[0].childNodes[0].data
    objects = root.getElementsByTagName("object")
    # print(f"img name: {imgName}")
    # print(f"img info(w, h, c): {imgW}, {imgH}, {imgC}")

    imgBox = []

    for box in objects:
        clsName = box.getElementsByTagName("name")[0].childNodes[0].data
        x1 = int(box.getElementsByTagName("xmin")[0].childNodes[0].data)
        y1 = int(box.getElementsByTagName("ymin")[0].childNodes[0].data)
        x2 = int(box.getElementsByTagName("xmax")[0].childNodes[0].data)
        y2 = int(box.getElementsByTagName("ymax")[0].childNodes[0].data)
        print(f"box: {clsName} {x1} {y1} {x2} {y2}")
        imgFileName = f"{imgXmlFile}.jpg"
        imgBox.append([clsName, x1, y1, x2, y2])
    print(f"imgBox: {imgBox}")  
    saveFile(imgXmlFile, [imgW, imgH], imgBox)

for file in files:
    print(f"file name: {file}")
    fileXml = file.split(".")
    getXmlData(annoPath, fileXml[0])
