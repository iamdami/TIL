import os


rtDir = "./"
firstLabelDirPath = f"{rtDir}a/"
secondLabelDirPath = f"{rtDir}b/"

firstLabelFileList = os.listdir(firstLabelDirPath)
secondLabelFileList = os.listdir(secondLabelDirPath)

def is_txt_files(path, ext = ".txt"):
    return {
        ent.name
        for ent in os.scandir(path)
        if ent.is_file() and ent.name.endswith(ext)
    }

firstLabelFile = is_txt_files(firstLabelDirPath, ".txt")
secondLabelFile = is_txt_files(secondLabelDirPath, ".txt")

for name in firstLabelFile.union(secondLabelFile):
    mergedLabelFile = os.path.join(f"{rtDir}mergedLabelFolder/", name)
    with open(mergedLabelFile, "a") as mergedFile:
        if name in firstLabelFile:
            firstFile = open(os.path.join(firstLabelDirPath, name))
            mergedFile.write(firstFile.read()+"\n")
        if name in secondLabelFile:
            secondFile = open(os.path.join(secondLabelDirPath, name))
            mergedFile.write(secondFile.read()+"\n")

# same function
"""
for name in firstLabelFile.union(secondLabelFile):
     mergedLabelFile = os.path.join(f"{rtDir}mergedLabelFolder/", name)
     with open(mergedLabelFile, "a") as mergedFile:
         if name in firstLabelFile:
             with open(os.path.join(firstLabelDirPath, name), "r") as firstFile:
                 shutil.copyfileobj(firstFile, mergedFile)
         if name in secondLabelFile:
             with open(os.path.join(secondLabelDirPath, name), "r") as secondFile:
                 shutil.copyfileobj(secondFile, mergedFile)
"""
