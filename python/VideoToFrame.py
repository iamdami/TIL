import cv2

vid = cv2.VideoCapture("path.MP4")
frameIdx = 0

while 1:
    ret, frame = vid.read()
    if not ret: 
        vid.release()
        break
    frameIdx += 1

    cv2.imwrite(f"path/{frameIdx}.jpg", frame)
