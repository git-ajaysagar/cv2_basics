#The following program detects yellow color in video frames using opencv

# -*- coding: utf-8 -*-
'''By Ajay'''

import cv2 as cv
import numpy as np

vid_feed=cv.VideoCapture(0)

while (1):
    _,frame=vid_feed.read()
    frame= cv.GaussianBlur(frame,(5,5),0)
    hsv= cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    low_range=np.array([20,100,100])
    upper_range=np.array([30,255,255])
    mask= cv.inRange(hsv, low_range,upper_range)
    output= cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow('frame',frame)
    cv.imshow('detected frames', output)
    k=cv.waitKey(10)
    if k==27:
        break

vid_feed.release()   
cv.destroyAllWindows()
