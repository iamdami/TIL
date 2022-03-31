import cv2
import numpy as np


# blue color
img = cv2.imread("./blueCloth.jpg")

hsvImg = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
lowerBlue = np.array([50, 40, 0])
upperBlue = np.array([130, 255, 255])
maskBlue = cv2.inRange(hsvImg, lowerBlue, upperBlue)

res = cv2.bitwise_and(img, img, mask=maskBlue)

cv2.imwrite("./img.jpg", img)
cv2.imwrite("./maskBlue.jpg", maskBlue)
cv2.imwrite("./res.jpg", res)
