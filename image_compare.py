#for colored images only

import cv2 as cv
import argparse

arg_ob=argparse.ArgumentParser()
arg_ob.add_argument("-i1","--image1",required=True,help="first image")
arg_ob.add_argument("-i2","--image2",required=True,help="second image")
image_args= vars(arg_ob.parse_args())

im1=cv.imread(image_args['image1'])
im2=cv.imread(image_args['image2'])

if im1.shape==im2.shape:
    diff=cv.subtract(im1,im2)
    print(diff)
    b,g,r=cv.split(diff)
    if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
        print('images are same')
else:
    print('images are different')


