import cv2
import imagesize

imgPath = "../../cocoToYoloFormat/train/images/000000168622_jpg.rf.f114faaa06c2b44134f479a97ca014ba.jpg"
img = cv2.imread(imgPath)

w, h = imagesize.get(str(imgPath))

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

# print(minX, minY, width, height)

minX2 = minX + width
minY2 = minY + height

# print(minX2, minY2)

recImg = cv2.rectangle(img, (minX, minY), (minX2, minY2), (255, 0, 0), 3)
cv2.imwrite("./recImg.jpg", recImg)
