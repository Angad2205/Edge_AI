import cv2 as cv
import numpy as np 
import os 
#capture frame from the camera 
cap = cv.VideoCapture(0)
harcascade = cv.CascadeClassifier('har_cascade.xml')
while True:
    ret , frame = cap.read()
    frame = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
    cv.imshow('vedio' , frame)

    if cv.waitKey(1) == ord('g'):
        break
