import cv2 as cv

img=cv.imread('Pictures\cat.jpeg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

thresholded= cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,50) #greater the c-value ie, more the diff from the mean, more accurate is the edge detection


cv.imshow('Adaptive Thresholding', thresholded)
cv.waitKey(0)
