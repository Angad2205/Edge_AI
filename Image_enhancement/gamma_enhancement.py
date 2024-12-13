import cv2 as cv
import numpy as np 

def log_enh(image, c):
    table = np.array([(np.log(i / 255 + 1) * c) * 255 for i in np.arange(0, 256)]).astype("uint8")   // c*log(i+1)
    return cv.LUT(image, table)

def gamma_enh(image, gamma):
    inverse = 1 / gamma
    table = np.array([(np.clip((i / 255) ** inverse, 0, 1) * 255) for i in np.arange(0, 256)]).astype("uint8")  // i^1/gamma
    return cv.LUT(image, table)

# Read the image
img = cv.imread('dark_image.jpg')  # Ensure the correct file extension

# Apply enhancements
img1 = log_enh(img, 2)
img2 = gamma_enh(img, 2)

# Display the results
cv.imshow("Log Enhancement", img1)
cv.imshow("Gamma Enhancement", img2)
cv.waitKey(0)
cv.destroyAllWindows()
