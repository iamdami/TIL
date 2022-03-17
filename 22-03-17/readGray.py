import cv2
from numpy import source

source = cv2.VideoCapture("night.mp4")
ret, img = source.read()
while True:

    if not ret:
        print("can't read video")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)

    cv2.imshow("nightGray", gray)

    wk = cv2.waitKey(10)
    if wk == ord("q"):
        break

cv2.destroyAllWindows()
source.release()