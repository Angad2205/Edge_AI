import cv2 as cv 
import numpy as np 
from time import time 
# Max filter using convolution
def max_filter(image, filter):
    row, column = image.shape
    row_1, column_1 = filter.shape
    row2 = row_1 // 2
    column2 = column_1 // 2
    result = np.zeros_like(image, dtype="float32")
    
    for i in range(row2, row - row2):
        for j in range(column2, column - column2):
            t = image[i - row2:i + row2 + 1, j - column2:j + column2 + 1]
            result[i, j] = np.max(t)
    
    return result

# Median filter using convolution
def median_filter(image, filter):
    row, column = image.shape
    row_1, column_1 = filter.shape
    row2 = row_1 // 2
    column2 = column_1 // 2
    result = np.zeros_like(image, dtype="float32")
    
    for i in range(row2, row - row2):
        for j in range(column2, column - column2):
            t = image[i - row2:i + row2 + 1, j - column2:j + column2 + 1]
            result[i, j] = np.median(t)
    
    return result

# Min filter using convolution
def min_filter(image, filter):
    row, column = image.shape
    row_1, column_1 = filter.shape
    row2 = row_1 // 2
    column2 = column_1 // 2
    result = np.zeros_like(image, dtype="float32")
    
    for i in range(row2, row - row2):
        for j in range(column2, column - column2):
            t = image[i - row2:i + row2 + 1, j - column2:j + column2 + 1]
            result[i, j] = np.min(t)
    
    return result

# Mean filter using convolution
def mean_filter(image, filter):
    row, column = image.shape
    row_1, column_1 = filter.shape
    row2 = row_1 // 2
    column2 = column_1 // 2
    result = np.zeros_like(image, dtype="float32")
    
    for i in range(row2, row - row2):
        for j in range(column2, column - column2):
            t = image[i - row2:i + row2 + 1, j - column2:j + column2 + 1]
            result[i, j] = np.mean(t)
    
    return result

# Example usage
image = np.random.random((10, 10)).astype(np.float32)  # Create a random image
filter = np.random.random((3, 3)).astype(np.float32)   # Create a random filter (not used in this context)

max_result = max_filter(image, filter)
median_result = median_filter(image, filter)
min_result = min_filter(image, filter)
mean_result = mean_filter(image, filter)

print("Max Filter Result:\n", max_result)
print("Median Filter Result:\n", median_result)
print("Min Filter Result:\n", min_result)
print("Mean Filter Result:\n", mean_result)

                       