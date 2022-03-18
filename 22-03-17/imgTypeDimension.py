import cv2

video = "./night.mp4" 
cap = cv2.VideoCapture(video)

if cap.isOpened():                 
    
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        if ret:                     
            cv2.imwrite("./origin.png",img)
            print(type(img), img, img.shape)
            
            cv2.imwrite("./gray.png", gray)
            print(type(gray), gray, gray.shape)
            break

        else:                      
            break                

else:
    print("can't open video")      

cap.release()                     
cv2.destroyAllWindows()
