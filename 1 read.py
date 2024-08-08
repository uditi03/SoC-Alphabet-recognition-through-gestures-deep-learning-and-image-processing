import cv2 as cv
#rescaling image; WORKS FOR ALL
def rescale(frame, scale=0.75):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions=(width,height) #tuple of dimension required
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) #resizes frame to dimensions

#changing resolution; WORKS ONLY FOR LIVE VIDEO(WEBCAM)
def resolution(capture, width, height, brightness=100):
    capture.set(3,width) #3 and 4 stand for properties of capture class
    capture.set(4,height)
    capture.set(10,brightness)

#reading images
def images():
    img= cv.imread("Pictures/cat.jpeg") #converts jpeg to matrix of pixels
    cv.imshow('Cat', img)
    print(img.shape) #displays image in a new window, cat is the name of the window and img is the matrix to diplay
    cv.waitKey(0) #keyboard binary function === waits for a key to be pressed; 0 means waits for infinite amount of time for a key to be pressed.

#reading videos
#captureWebcam=cv.VideoCapture(0) 
def videos():
    capture= cv.VideoCapture('Videos/cat.mp4') #capturing video
    while True:
        success, frame= capture.read()  #reading the video frame by frame
        #When a frame is successfully read, read() returns a tuple containing two elements:
        #isTrue: This is a pre-defined boolean set to True by the function itself.
        #frame: This variable stores the actual image data of the captured frame
        # frame_resized= rescale(frame)
        cv.imshow('Video', frame)
        # cv.imshow('VideoResized', frame_resized) #passing the resized frame to be shown
        
        if cv.waitKey(20) & 0xFF==ord('d'): #if d key is pressed
            break
    capture.release()
    cv.destroyAllWindows()
    
def videos_webcam():
    
    capture= cv.VideoCapture(0)
    resolution(capture,100,100)
    while True:
        success, frame=capture.read()
        
        cv.imshow("Webcam",frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    capture.release()
    cv.destroyAllWindows
   

videos()
