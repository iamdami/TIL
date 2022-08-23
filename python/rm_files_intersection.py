import os


rtDir = "./"
allImgDirPath = f"{rtDir}a/"
cocoCarImgDirPath = f"{rtDir}b/"

allImgFileList = os.listdir(allImgDirPath)
cocoCarImgFileList = os.listdir(cocoCarImgDirPath)

def is_img_files(path, ext = ".jpg"):
    return {
        ent.name
        for ent in os.scandir(path)
        if ent.is_file() and ent.name.endswith(ext)
    }

allImgFile = is_img_files(allImgDirPath, ".jpg")
print(allImgFile)
cocoCarImgFile = is_img_files(cocoCarImgDirPath, ".jpg")
print(cocoCarImgFile)
for name in allImgFile.intersection(cocoCarImgFile):
    if name in allImgFile:
        print("name in allImgFile")
        os.remove(os.path.join(allImgDirPath, name))
    # if name in cocoCarImgFile:
    #     print("name in cocoCarImgFile")
    #     os.remove(os.path.join(cocoCarImgDirPath, name))
