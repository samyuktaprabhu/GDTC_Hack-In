import numpy as np 
import cv2
cap=cv2.VideoCapture(0)
success,image = cap.read() 
count = 0
success = True
while success:
    success,image = cap.read()
    print('Read a new frame: ', success)    #reading frame
    cv2.imwrite("Frame%d.jpg" % count, image)     # save frame as JPEG file
    count += 1
    cv2.imshow('img',image)
    cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
