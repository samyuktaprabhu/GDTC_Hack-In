import numpy as np
import cv2
import time 
cap = cv2.VideoCapture(0)
time.sleep(1)
background = 0
count = 0
for i in range(60):
    ret, background = cap.read()
background = np.flip(background, axis=1)

while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lr = np.array([0, 120, 70])
    ur= np.array([10, 255, 255])
    m1 = cv2.inRange(hsv, lr, ur) 
    lr = np.array([180, 110, 100])
    ur = np.array([255, 191, 180])
    m2 = cv2.inRange(hsv, lr, ur)
    m1 = m1 + m2 
    m1 = cv2.morphologyEx(m1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    m1 = cv2.morphologyEx(m1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)        
    m2 = cv2.bitwise_not(m1)
    r1 = cv2.bitwise_and(background, background, mask = m1)
    r2 = cv2.bitwise_and(img, img, mask = m2)
    final = cv2.addWeighted(r1, 1, r2, 1, 0)
    cv2.imshow('BeingInvisible', final)
    k = cv2.waitKey(5)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
