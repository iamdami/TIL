import cv2
import imagesize

imgPath = ""
img = cv2.imread(imgPath)

w, h = imagesize.get(str(imgPath))

# yolo bbox value
xCenter = 0.4921875
yCenter = 0.5958333333333333
width = 0.303125
height = 0.75

float_xCenter = w * xCenter
float_yCenter = h * yCenter
float_width = w * width
float_height = h * height

minX = int(float_xCenter - (float_width / 2))
minY = int(float_yCenter - (float_height / 2))
width = int(float_width)
height = int(float_height)

minX2 = minX + width
minY2 = minY + height

recImg = cv2.rectangle(img, (minX, minY), (minX2, minY2), (255, 0, 0), 3)
cv2.imwrite("./recImg.jpg", recImg)
