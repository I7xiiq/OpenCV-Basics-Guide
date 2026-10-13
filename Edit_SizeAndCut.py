import cv2 as cv

# Read the image from the file
img = cv.imread('myimage1.jpeg')

# Get the dimensions of the image (height, width, channels)
imgSize = img.shape
print(imgSize) # (349 = height(y), 627 = width(x), 3 = color channels BGR)

# Resize the image to a new width and height (400x400 pixels)
imgResize = cv.resize(img , (400, 400))

# Crop the image using array slicing [start_y:end_y, start_x:end_x]
imgCrop = img[0:200, 200:400]

# Display the original, resized, and cropped images in separate windows
cv.imshow('img' , img) 
cv.imshow('img resize' , imgResize) 
cv.imshow('img crop' , imgCrop) 

# Wait infinitely until any key is pressed to close the windows
cv.waitKey(0)