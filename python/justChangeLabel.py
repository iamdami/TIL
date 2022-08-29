import os

labelPath = "labels_car_plate/"
labelSavePath = "labels/"
labelFileList = os.listdir(labelPath)

for labelFile in labelFileList:
    labelFilePath = os.path.join(labelPath, labelFile)
    labelFileSavePath = os.path.join(labelSavePath, labelFile)
    with open(labelFilePath, "r") as f:
        labelFile = f.readlines()
    with open(labelFileSavePath, "a") as a:
        for labelLine in labelFile:
            labelLineList = labelLine.split(" ")
            if labelLineList[0] == "2":
                labelLineList[0] = "0"  # car
            elif labelLineList[0] == "6":
                labelLineList[0] = "1"  # plate
            else:
                print(f"wrong label file: {labelFilePath}")
            labelLineListStr = " ".join(labelLineList)
            a.write(labelLineListStr)
