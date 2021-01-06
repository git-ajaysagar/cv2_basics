#Changing background (single color) in an image using opencv

# -*- coding: utf-8 -*-
'''By Ajay'''

#importing opencv
import cv2 as cv

#loading image as an array
im=cv.imread('path to image')

#changing pixel values of image array
for p in im:
    for pp in p:
        if (pp==[250,224,170]).all()==True:
            pp[pp==[250,224,170]]=[0,159,246]

#saving altered image
cv.imwrite('changed_image.jpg',im)
