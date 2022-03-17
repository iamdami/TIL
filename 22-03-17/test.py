import cv2
import numpy as np

def video2frame(invideofilename, save_path):
    vidcap = cv2.VideoCapture(invideofilename)
    count = 0

    while True:
      success,image = vidcap.read()
      

      if not success:
          print("can't read video")
          break
      
      print ('Read a new frame: ', success)
      fname = "{}.jpg".format("{0:05d}".format(count))
      # grayImg = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2GRAY)
      cv2.imwrite(save_path + fname, image)
      count += 1
    print("{} images are extracted in {}.". format(count, save_path))


def main():
    
    video2frame("./night.mp4", "./brightness/")

if __name__ == "__main__":
    main()