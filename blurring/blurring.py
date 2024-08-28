import cv2 as cv 
import numpy as np
path = '1.png'
img = cv.imread(path)
cv.imshow('Stop sign' , img)

#Averaging technique

average  = cv.blur(img , (9,9))
cv.imshow('blur image' , average)

# Gaussian blurr 

blur = cv.GaussianBlur(img , (9,9) , 0)
cv.imshow('Gaussian blur' , blur)

median = cv.medianBlur(img , 5)
cv.imshow('median blur' , median)

bilateral = cv.bilateralFilter(img , 10 , 35 , 25)
cv.imshow('bilateral' , bilateral)

cv.waitKey(10000)

