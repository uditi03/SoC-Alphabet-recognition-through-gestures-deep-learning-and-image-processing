import numpy as np
import cv2 as cv

img= cv.imread("Pictures/cat.jpeg")

def show(name, img):
    cv.imshow(name,img)
    cv.waitKey(0) 
    if 0xff=='d' :
        quit

def contours():
    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    show('Gray',gray)
    canny= cv.Canny(img,125,175)
    show('canny',canny)
    
contours()

