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


#displaying a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

#displaying a circle
cv.circle(blank, (250, 250), 40, (255, 0, 0), thickness=-1)
cv.imshow('Circle', blank)  # Display the circle

#displaying a line
cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)  # Display the line

#writing text
cv.putText(blank, 'Hello atish', (255, 255), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), thickness=2)
cv.imshow('Text', blank)  # Display the text

# Wait indefinitely for a key press before closing the windows
cv.waitKey(0)