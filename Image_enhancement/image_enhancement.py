import cv2 as cv 
import numpy as np

def log_inh(image, c):
    # Create the lookup table for logarithmic enhancement
    table = np.array([(np.log((i / 255.0) + 1) * c) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv.LUT(image, table)

# Read and resize the image
img = cv.imread('dark_image.jpg')
img = cv.resize(img, (500, 500))

# Apply logarithmic enhancement
img1 = log_inh(img, 2)

# Display the original and enhanced images
cv.imshow('Log Enhancement Image', img1)
cv.imshow('Original Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
