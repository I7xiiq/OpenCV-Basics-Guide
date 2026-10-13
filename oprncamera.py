import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    _, frame, = cap.read()
    cv.imshow('vid', frame)
    cv.waitKey(1)