#The following program detects faces using opencv dnn and tkinter GUI

# -*- coding: utf-8 -*-
'''By Ajay'''

import cv2
import numpy as np
from PIL import ImageTk
from tkinter import *
from PIL import Image as pim

modelFile = "C:\\Users\\Ajay\\models\\res10_300x300_ssd_iter_140000.caffemodel"
configFile = "C:\\Users\\Ajay\\models\\deploy.prototxt"

net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

#initiating a tkinter window
k=Tk()
k.config(background='#ffd800')

heading=Label(k,font=('Arial',15,'bold'),text='Face Detector',bg='#FC773E')
heading.place(relx=0.45, rely=0.13)

imageFrame = Frame(k)
imageFrame.place(relx=0.5,rely=0.18,anchor='n')

frame_label = Label(imageFrame)
frame_label.grid(row=0, column=0)

def face():
    _,img=cap.read()
    face_list=[]
    face_list.clear()
    h, w = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,
    (300, 300), (104.0, 117.0, 123.0))
    net.setInput(blob)
    faces = net.forward()
    #to draw box around face on image
    for i in range(faces.shape[2]):
        try:
            confidence = faces[0, 0, i, 2]
            if confidence > 0.5:
                face_list.append('face')
                box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x, y, x1, y1) = box.astype("int")
                cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
                detected_face=img[y:y1,x:x1]
                detected_face=cv2.resize(detected_face,(160,160),cv2.INTER_AREA)
    
        except:
            pass
    if len(face_list)==0:
        label1=Label(k,text=' No face detected!  ',font=('arial' ,20),bg='#d279a6',fg='black')
        label1.place(relx=0.75,rely=0.2)
    else:
        label1=Label(k,text='Face detected o_O',font=('arial',20),bg='#d279a6',fg='white')
        label1.place(relx=0.75,rely=0.2)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGBA)
    img=pim.fromarray(img) 
    img=ImageTk.PhotoImage(image=img)
    frame_label.image=img
    frame_label.configure(image=img)
    frame_label.after(100,face)
def close():
    k.destroy()
    
close_button=Button(k,text='close x',command=close,bg='#fc3e64')
close_button.place(relx=0.5,rely=0.9)

cap=cv2.VideoCapture(0)
face()
k.mainloop()
cap.release()
