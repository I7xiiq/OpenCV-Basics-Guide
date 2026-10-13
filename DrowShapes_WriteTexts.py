import cv2 as cv
import numpy as np

# Create a blank black image (Height=600, Width=800, 3 color channels)
img = np.zeros((600, 800, 3), np.uint8)

# img[:] = 0, 0, 255  # If uncommented, this fills the whole image with Red color (BGR format)

# --- Draw Shapes ---

# Draw a specific line - currently commented out
# cv.line(img , (0,0) , (400,550), (255,0,0) , 2) 

# Draw a Blue line across the whole image (from top-left to bottom-right)
cv.line(img, (0,0), (img.shape[1], img.shape[0]), (255,0,0), 2)

# Draw a Green rectangle from point (50,50) to (400,400) with thickness 2
cv.rectangle(img, (50,50), (400,400), (0,255,0), 2)

# Draw a Red circle at center (300,300) with radius 100
cv.circle(img, (300,300), 100, (0,0,255), 2)

# --- Add Text ---

# Write text starting at (400,500) with Purple color and font scale 1
cv.putText(img, 'OPENCV SALAR_DEV', (400,500), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,255), 1)

# Display the final image in a window
cv.imshow('img', img) 

# Wait infinitely until any key is pressed
cv.waitKey(0)