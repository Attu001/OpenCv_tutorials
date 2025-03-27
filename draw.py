import cv2 as cv
import numpy as np

# Create a blank image (500x500 pixels, 3 color channels, uint8 data type)
blank = np.zeros((500, 500, 3), dtype='uint8')

# Display the blank image in a window named 'Blank'
cv.imshow('Blank', blank)

# Fill the entire blank image with green color (BGR: 0, 255, 0)
blank[:] = 0, 255, 0

# Display the green image in a window named 'Green'
cv.imshow('Green', blank)

# Wait indefinitely for a key press before closing the windows
cv.waitKey(0)