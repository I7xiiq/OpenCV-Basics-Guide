import cv2 as cv
import numpy as np

img1 = cv.imread('myimage1.jpeg')
img2 = cv.imread('images.jpeg')


cv.imshow('img' , img1)
cv.imshow('img2' , img2)


cv.waitKey(0)