from cmath import isfinite
import os
import os.path
import glob


dirPath = "labels/val/"
fileName = "*.txt"
inputNum = input("your file Num : ")
print(inputNum.isdigit())
lableFileList = glob.glob(dirPath + fileName)
print(len(lableFileList))
if inputNum.isdigit() and len(lableFileList) == int(inputNum):
    for lableFile in lableFileList:
        # print(lableFile)
        with open(lableFile, "r") as f:
            data = f.read()
        data = data.replace("3 ", "2 ")
        print(data)

        with open(lableFile, "w") as f:
            f.write(data)
else:
    print(f"your file Num : {len(lableFileList)}")
    print("or your input type not int")
