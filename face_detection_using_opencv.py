#The following program detects faces using opencv

# -*- coding: utf-8 -*-
'''By Ajay'''

#importing necessasry libraries
import cv2 as cv

#starting camera and detecting faces using haarcascade
try:
    vid_detect = cv.VideoCapture(0)
    while 1:
        _,frame=vid_detect.read()
        
        #loading haarcascade xml file to detect faces 
        cascade = cv.CascadeClassifier('C:\\Users\\Ajay\\Anaconda3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
    
        # Applying the haar classifier to detect faces
        face_coord = cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=12)
        for (x, y, w, h) in face_coord:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv.imshow('detected', frame)
        k=cv.waitKey(10)
        if k== 27:
            break
except:
    pass       

vid_detect.release()
cv.destroyAllWindows()  