# use float number as opencv image pixel coordinates

import cv2
import numpy as np

img = cv2.imread('myimage.png')
interpolated_pixel = cv2.remap(img, np.array([[2.4]], np.float32), np.array([[5.4]], np.float32), cv2.INTER_LINEAR)
print(interpolated_pixel)
