import cv2 as cv
import numpy as np

# Read the image from the file
img = cv.imread('photos/bcat.jpg')
# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)  # Display the original image

contors= heirarchy = cv.findContours(gray, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  # Find contours in the image

cv.waitKey(0)  # Wait indefinitely for a key press