import cv2

vid = cv2.VideoCapture("path/.mp4")
ret, frame = vid.read()
frameCnt = 1000  # set start frame
vid.set(cv2.CAP_PROP_POS_FRAMES, frameCnt)

while ret:
    ret, frame = vid.read()
    frameCnt += 1
    cv2.imwrite(f"path/{frameCnt}.jpg", frame) 
    print('Read frame : ', frameCnt)
    if frameCnt == 1100:  # set end frame
        break
