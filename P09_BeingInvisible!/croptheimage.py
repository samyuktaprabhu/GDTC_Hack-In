import numpy as np 
import cv2
success = True
while success:
    #success,image = cap.read()
    img=cv2.imread('frame10.jpg')
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    image = gray[200:400,300:600]
    print('Cropped')    #reading frame
    cv2.imwrite("Frame0.jpg", image)     # save frame as JPEG file
    success=False
    cv2.imshow('img',image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
