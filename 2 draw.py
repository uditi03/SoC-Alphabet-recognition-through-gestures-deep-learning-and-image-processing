import cv2 as cv
import numpy as np

def show(name, img):
    cv.imshow(name,img)
    cv.waitKey(0) 
    if 0xff=='d' :
        quit

blank= np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank',blank)

# img=cv.imread('Pictures\cat.jpeg')
# cv.imshow('Cat',img)

#cv.waitKey(0)

def full_color(blank):
    blank[:]= 0,255,0 #selecting all columns and rows of blank array and setting to green
    cv.imshow('Green',blank)
    cv.waitKey(0)

def area_color(blank):
    blank[200:300, 300:400]= 0,0,255
    blank[100:200, 300:400]= 255,0,0
    blank[200:300, 100:200]= 0,255,0
    show("Mix", blank)

def rect():
    cv.rectangle(blank.copy(), (0,0), (blank.shape[0]//2, blank.shape[1]//2) ,  (0,255,0), thickness=-1) #cv.FILLED replacement for -1
    #shape[0]=width, shape[1]=height, shape[2]=height as mentioned in the initialisation of blank
    show('Rectangle', blank)

def cir():
   
    cv.circle(blank.copy(), (blank.shape[0]//2, blank.shape[1]//2), 100, (255,0,0), thickness=50 )
    show('Circle', blank)
    
def lin():
    cv.line(blank.copy(), (0,0), (blank.shape[0]//2, blank.shape[1]//2), (255,255,0), thickness=20)
    show('Line', blank)

def text():
    cv.putText(blank.copy(), 'YoYo', (blank.shape[0]//2-80, blank.shape[1]//2 ),  cv.FONT_HERSHEY_TRIPLEX, 2.0, (255,255,0), 4 )
    show('Text_On_Image',blank)



#area_color()
#cir()
area_color(blank)


