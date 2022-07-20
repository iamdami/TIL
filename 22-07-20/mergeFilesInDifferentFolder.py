import os
import shutil


rtDir = "./"
carLabelDirPath = f"{rtDir}carTestFolder/"
plateLabelDirPath = f"{rtDir}plateTestFolder/"

carLabelFileList = os.listdir(carLabelDirPath)
plateLabelFileList = os.listdir(plateLabelDirPath)

def is_txt_files(path, ext = ".txt"):
    return {
        ent.name
        for ent in os.scandir(path)
        if ent.is_file() and ent.name.endswith(ext)
    }

carLabelFile = is_txt_files(carLabelDirPath, ".txt")
plateLabelFile = is_txt_files(plateLabelDirPath, ".txt")

for name in carLabelFile.union(plateLabelFile):
    mergedLabelFile = os.path.join(f"{rtDir}mergedLabelFolder/", name)
    with open(mergedLabelFile, "a") as mergedFile:
        if name in carLabelFile:
            with open(os.path.join(carLabelDirPath, name), "r") as carFile:
                shutil.copyfileobj(carFile, mergedFile)
        if name in plateLabelFile:
            with open(os.path.join(plateLabelDirPath, name), "r") as plateFile:
                shutil.copyfileobj(plateFile, mergedFile)
