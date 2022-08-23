import glob
import os

labelPath = "./a/"
imgPath = "./b/"
fileFormat = "*.txt"
labelFileList = glob.glob(labelPath + fileFormat)
for labelFile in labelFileList:
    with open(labelFile,"r+") as f:
        data = f.readlines()
        f.seek(0)
        new_line = list()
        
        # remove line if specific data is not exist in the line
        for line in data:
            if "2 " not in line:
                f.write(line)
            line = line.replace(' ','')
            line = line.replace('\n','')
            new_line.append(line)
        f.truncate()
        
        # remove file and image with the same name of file if the file hasn't any useful data
        imgFileName = labelFile.split("/")[-1].split(".")[0] + ".jpg"
        imgFilePath = os.path.join(imgPath, imgFileName)
        if len(new_line) == 1 and '' in new_line or len(new_line) == 0:
            os.remove(labelFile)
            os.remove(imgFilePath)
