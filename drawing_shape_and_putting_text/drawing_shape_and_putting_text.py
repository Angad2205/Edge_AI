import cv2 as cv
import numpy as np

# to create the blank screen to work with and setting pixel values to zero to get black screen 

blank = np.zeros((500,500,3) , dtype = 'uint8')
cv.imshow('blank' , blank)

# now we will paint the frame into green by manupilating the data stored in the blank variable in the form of matrix 

blank[:] = 0,255,0

cv.imshow('green',blank)


# Draw rectangle using the cv.rectangle function 

cv.rectangle(blank, (0,0) , (250,250) , (0,0,255) , thickness = 2)
cv.imshow('rectangle' , blank)

# Draw circle using open cv
cv.circle(blank , (250,250) , 40, (255,0,0) , thickness = 3)
cv.imshow('circle' , blank)

#Draw line on the image 

cv.line(blank , (0,0) , (500,500) , (255,255,255) , thickness = 5)
cv.imshow('line' , blank)

# writing text on the image 
cv.putText(blank , 'Hello' , (255,255), cv.FONT_HERSHEY_TRIPLEX , 1.0 , (0,0,255) , 2)
cv.imshow('text' , blank) 
cv.waitKey(5000)


