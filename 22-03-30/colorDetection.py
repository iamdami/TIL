import cv2
import numpy as np


img = cv2.imread(".jpg")                

# Convert BGR to HSV
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define color range
color1 = np.array([24,150,50])
color2 = np.array([130,170,255])

# Threshold the HSV img to get colors only you want
mask = cv2.inRange(hsvImg, color1, color2)

# Bitwise-AND mask and original image
outputImg = cv2.bitwise_and(img, img, mask = mask)
    
cv2.imshow("Color Detected", np.hstack((img, outputImg)))
cv2.waitKey(0)
cv2.destroyAllWindows()
