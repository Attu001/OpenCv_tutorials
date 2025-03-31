import cv2 as cv
import numpy as np

# Read the image from the file
img = cv.imread('photos/bcat.jpg')
# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)  # Display the original image

# # Apply Gaussian blur to the grayscale image to reduce noise and improve edge detection
# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)  # Apply Gaussian blur

# canny=cv.Canny(blur, 125, 175)  # Apply Canny edge detection
# cv.imshow('canny', canny)  # Display the edges detected

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)  # Apply binary thresholding
cv.imshow('thresh', thresh)  # Display the thresholded image

countors, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  # Find contours in the edge-detected image
print(len(countors))  # Print the contours found



cv.waitKey(0)  # Wait indefinitely for a key press