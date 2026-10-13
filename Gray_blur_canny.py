import cv2 as cv

# Read the image from the file
img = cv.imread('myimage1.jpeg')

# Convert the image to Grayscale (black and white)
imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply Gaussian blur to smooth the image and reduce noise
imgblur = cv.GaussianBlur(imggray, (9, 9), 0)

# Find edges in the image using Canny Edge Detection
imgcanny = cv.Canny(img, 200, 200)

# Show all the images in separate windows
cv.imshow('image', img)
cv.imshow('gray img', imggray)
cv.imshow('blur img', imgblur)
cv.imshow('Canny img', imgcanny)

# Wait indefinitely until any key is pressed before closing windows
cv.waitKey(0)