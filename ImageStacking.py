import cv2 as cv
import numpy as np

# Read the first and second images
img1 = cv.imread('myimage1.jpeg')
img2 = cv.imread('images.jpeg')

# Resize img2 to match the exact dimensions of img1 (Width, Height)
# This step is required before stacking them
img2_resize = cv.resize(img2, (img1.shape[1], img1.shape[0]))

# Stack the two images Horizontally (side by side)
imgH = np.hstack((img1, img2_resize))

# Stack the two images Vertically (one on top of the other)
imgV = np.vstack((img1, img2_resize))

# Display the original and the stacked images in separate windows
cv.imshow('img', img1)
cv.imshow('img2', img2)
cv.imshow('imgh', imgH)
cv.imshow('imgv', imgV)

# Wait infinitely until any key is pressed to close the windows
cv.waitKey(0)