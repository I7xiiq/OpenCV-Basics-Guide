import cv2 as cv

img = cv.imread('myimage1.jpeg')

imgSize = img.shape
print(imgSize) #(349=y , 627=x , 3=BGR)

#resize
imgResize = cv.resize(img , (400,400))


imgCrop = img[0:200 , 200:400]

cv.imshow('img' , img) 
cv.imshow('img resize' , imgResize) 
cv.imshow('img crop' , imgCrop) 


cv.waitKey(0)