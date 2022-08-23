from cmath import isfinite
import os
import os.path
import glob


dirPath = "labels/val/"
fileName = "*.txt"
inputNum = input("your file Num : ")
print(inputNum.isdigit())
labelFileList = glob.glob(dirPath + fileName)
print(len(labelFileList))
if inputNum.isdigit() and len(labelFileList) == int(inputNum):
    for labelFile in labelFileList:
        with open(labelFile, "r") as f:
            data = f.read()
        data = data.replace("3 ", "2 ")
        print(data)

        with open(labelFile, "w") as f:
            f.write(data)
else:
    print(f"your file Num : {len(labelFileList)}")
    print("or your input type not int")
