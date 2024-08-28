import cv2 as cv
import numpy as np
path = '1.png'
img = cv.imread(path)
cv.imshow('picture' , img)

gray = cv.cvtColor(img , cv.COLOR_RGB2GRAY)
cv.imshow('gray' , gray)

#BGR TO HSV (huge saturation value)
HSV = cv.cvtColor(img , cv.COLOR_BGR2HSV)
cv.imshow('hsv' , HSV)

# BGR TO LAB
lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)
cv.imshow('LAB' , lab)


# splitting the image in B G R COLOUR CHANNEL to test the intensity of each channel but it will be displayed in the grey scale format  

b,g,r = cv.split(img)
cv.imshow('blue' , b)
cv.imshow('green' , g)
cv.imshow('red' , r)

merge = cv.merge([b,g,r])  # using this function we can get the orginal picture again by merging the three color channel 
cv.imshow('merge' , merge)

# creating the blank channel of 500X500 pixel 
blank = np.zeros((img.shape[:2]) , dtype ='uint8') 
#here we are creating the image to show the different colour channel in the image by first creating the blank image and mixing the image using the different colour channel , we are taking only two values so that we only get the info about the height and width of the image not the info of colour channel 

blue = cv.merge([b , blank , blank])
green = cv.merge([blank , g , blank])
red = cv.merge([blank , blank , r])

cv.imshow('blue' , blue)
cv.imshow('green' , green)
cv.imshow('red' , red)

cv.waitKey(10000)

