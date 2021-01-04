#The following program detects yellow color objects and draws contour around them, in video feed using opencv

# -*- coding: utf-8 -*-
'''By Ajay'''

import cv2 as cv
import numpy as np

img=cv.VideoCapture(0)
while True:
    _,frame=img.read()
    frame= cv.GaussianBlur(frame,(5,5),0)
    hsv= cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_range=np.array([20,100,100])
    upper_range=np.array([30,255,255])
    mask= cv.inRange(hsv, lower_range,upper_range)
    contours,_ = cv.findContours(mask,cv.RETR_TREE, cv.CHAIN_APPROX_NONE) 
    for contour in contours:
        con_area=cv.contourArea(contour)
        if con_area>=100:
            cv.drawContours(frame, contour, -1, (0, 255, 0), 3) 
    
    cv.imshow('img',frame)
    k=cv.waitKey(10)
    if k==27:
        break
img.release()  
cv.destroyAllWindows()
