import cv2 as cv

img = cv.imread("myimage1.jpeg")
cv.imshow('image', img)
cv.waitKey(0)