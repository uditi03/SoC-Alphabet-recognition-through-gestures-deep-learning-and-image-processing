import cv2 as cv
import numpy as np
def show(name, img):
    cv.imshow(name,img)
    cv.waitKey(0) 
    if 0xff=='d' :
        quit 
    
img= cv.imread("Pictures/cat.jpeg")
rows,cols=img.shape[:2] #returns a tuple like: (rows,cols,channels: axis=0,axis=1,colorChannels)
#same as writing:
#rows=img.shape[0], cols=img.shape[1]
dim =(rows,cols)


#translation
def translate(img,x,y):
    #make a translation matrix :
    transMat=np.float32([[1,0,x],[0,1,y]]) 
    #1,0,x= scaling in x,change in horizontal distance between any two pixels during translation, x=shift in x 
    # 0,1,y= change in ver dist bw any 2 px, scaling in y, shift in y
    return cv.warpAffine(img,transMat,dim)


# cv.imshow("translate",translated)


#rotation
def rotation(img,angle,rotPoint=None):
    if rotPoint is None:
        rotPoint=(rows//2, cols//2)
    rotMat= cv.getRotationMatrix2D(rotPoint,angle,1.0)
    return cv.warpAffine(img,rotMat,dim)

def flipping():
    flip= cv.flip(img,-1) #0=flip about x axis,1=y,-1=both
    show('flip',flip)

def cropping():
    cropped=img[100:400, 200:400] #index slicing
    show('Crop',cropped)

show('og',img)
translated=translate(img,100,100)
show('translated',translated)
