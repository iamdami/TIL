import cv2 
import os 
import glob 
img_dir = "" # Enter Directory of all images  
data_path = os.path.join(img_dir,'*g') 
files = glob.glob(data_path) 
data = [] 
for i in files: 
    img = cv2.imread(i) 
    data.append(img) 
