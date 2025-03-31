import cv2 as cv
import numpy as np

# Read the image from the file
img = cv.imread('photos/bcat.jpg')

# Resize the image to 500x500 pixels
resized = cv.resize(img, (500, 500))

# Convert the image to grayscale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

# Apply binary thresholding
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)  # Display the thresholded image

# Find contours in the thresholded image
contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"Number of contours: {len(contours)}")  # Print the number of contours found

# Create a blank image with the same shape as the resized image
blank = np.zeros(resized.shape, dtype='uint8')

# Draw all contours on the blank image in red
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours', blank)  # Display the image with contours drawn

# Resize the blank image before displaying it
resized_blank = cv.resize(blank, (250, 250))  # Resize to 250x250 pixels
cv.imshow('Resized Contours', resized_blank)  # Display the resized image

cv.waitKey(0)  # Wait indefinitely for a key press
cv.destroyAllWindows()
