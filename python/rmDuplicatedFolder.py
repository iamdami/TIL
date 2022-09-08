import os, shutil

lfwPath = "/home/ubuntu/lfw_test/lfw/"
elderPath = "/home/ubuntu/elder_test/elderlyPpl/"

lfwPathNameList = os.listdir(lfwPath)
elderPathNameList = os.listdir(elderPath)

for i, lfwPathName in enumerate(lfwPathNameList):
    lfwPathNameList[i] = lfwPathName.split('.')[0]

for i, elderPathName in enumerate(elderPathNameList):
    elderPathNameList[i] = elderPathName.split('.')[0]

for lfwPathName in lfwPathNameList:
    if lfwPathName in elderPathNameList:
        shutil.rmtree(os.path.join(lfwPath, lfwPathName), ignore_errors=True)
        print(f"lfwPathName: {lfwPathName}")

for elderPathName in elderPathNameList:
    if elderPathName in lfwPathNameList:
        shutil.rmtree(os.path.join(elderPath, elderPathName), ignore_errors=True)
        print(f"elderPathName: {elderPathName}")
