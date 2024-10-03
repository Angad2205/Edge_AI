import cv2 as cv
import os 
# read the image 
i = cv.imread('sample.png')
#selecting roi 
v = cv.selectROI(i)

#i[int(v[1]):int(v[1]+v[3]),int(v[0]):int(v[0]):int(v[2]),0] = 0 
#i[int(v[1]):int(v[1]+v[3]),int(v[0]):int(v[0]):int(v[2]),1] = 0 
#i[int(v[1]):int(v[1]+v[3]),int(v[0]):int(v[0]):int(v[2]),2] = 255

roi = i[int(v[1]):int(v[1]+v[3]),int(v[0]):int(v[0]+v[2])]
cv.imshow('selected roi', roi)
cv.waitKey(0)
cv.destroyAllWindows()
print("hello")