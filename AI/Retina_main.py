import cv2,copy
import face_Information as fi
import detect

def main():
    global listface
    # model initialization
    FD_Net, FV_Net, Landmark_Net = fi.Initialization()
    rawImg = cv2.imread('.jpg')
    valImg = cv2.imread('.jpg')
    imgFaceDictList = detect.damiFaceDetect(rawImg)

    print(f"num of detected faces : {len(imgFaceDictList)}")
    
    if len(imgFaceDictList) == 0:
        print("didn't detected at all")
        exit 
        
    # Enroll Face
    for i, imgFaceDict in enumerate(imgFaceDictList):
        fi.Face_Enrollment(FV_Net, rawImg, imgFaceDict, i, "ID", i)
        print(f"listface{i} enrolled")
        
    # Verification
    valDictList = detect.damiFaceDetect(valImg)
    
    for i, valDict in enumerate(valDictList):
        sID,simMax = fi.Face_Verification(FV_Net, valImg, valDict, i)
        print(f"listface{i} %s : %.2f" % (sID, simMax))
        print("Done")


if __name__ == "__main__":
    main()
