import cv2 as cv


# For image
# img = cv.imread("myimage1.jpeg")
# cv.imshow('image', img)
# cv.waitKey(0)

# For Video
cap = cv.VideoCapture('myvid1.mp4')
while True:
    _, frame = cap.read()
    cv.imshow('video' , frame)
    cv.waitKey(5)