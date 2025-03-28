import cv2 as cv

img=cv.imread('photos/bcat.jpg')  # Read the image from the file

rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)  # Convert the image to RGB format

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY ) # Convert the image to grayscale


def rescaleFrame(frame, scale=0.2):
    # Calculate new width and height based on the scale
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # Resize the frame and return it
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resizedimg=rescaleFrame(rgb, scale=0.2)  # Rescale the image  
cv.imshow('cat', resizedimg)  # Display the original image

newresizedimg=rescaleFrame(gray, scale=0.2)  # Rescale the image
cv.imshow('cat2', newresizedimg)  # Display the grayscale image


blurresizedimg=rescaleFrame(img, scale=0.2)  # Rescale the image
newblurimg=cv.GaussianBlur(blurresizedimg, (7, 7), cv.BORDER_DEFAULT)  # Apply Gaussian blur to the image
cv.imshow('cat3', newblurimg)  # Display the blurred image


finedege=cv.Canny(resizedimg, 125, 175)  # Apply Canny edge detection to the image
cv.imshow('cat4', finedege)  # Display the edge-detected image

#dialating the image
dilatedimg=cv.dilate(finedege, (7, 7), iterations=3)  # Dilate the edges in the image
cv.imshow('cat5', dilatedimg)  # Display the dilated image

#eroding the image
erodedimg=cv.erode(dilatedimg, (7, 7), iterations=3)  # Erode the dilated image
cv.imshow('cat6', erodedimg)  # Display the eroded image

#resized
newhello=cv.resize(img, (500, 500))  # Resize the original image to 500x500 pixels
cv.imshow('cat7', newhello)  # Display the resized image

#cropping the image
height, width = img.shape[:2]  # Get the height and width of the original image
print(height, width)  # Print the dimensions of the image
croppedimg=img[50:200, 200:400]  # Crop the image to a specific region
cv.imshow('cat8', croppedimg)  # Display the cropped image

cv.waitKey(0)  # Wait indefinitely for a key press
