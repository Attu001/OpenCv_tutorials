
import cv2 as cv
import numpy as np  

cv.imread('photos/bcat.jpg')  # Read the image from the file
img=cv.imread('photos/bcat.jpg')  # Read the image from the file

#TRANSLATION
def translate(img, x, y):
    # Create a translation matrix
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    # Apply the translation to the image
    return cv.warpAffine(img, transMat, (img.shape[1], img.shape[0]))

#-x and -y for left and up translation
# +x and +y for right and down translation

def rescalingFrame(frame, scale=0.5):
    # Calculate new width and height based on the scale
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # Resize the frame and return it
    return cv.resize(frame, dimensions, interpolation=cv.INTER_CUBIC)

translateddown = translate(rescalingFrame(img), 100, 100)  # Translate the image by (100, 100) pixels
cv.imshow('Translated', translateddown)  # Display the translated image

translatedup = translate(rescalingFrame(img), -100, 100)  # Translate the image by (-100, -100) pixels
cv.imshow('Translatedup', translatedup)  # Display the translated image

def rotate(img,angle, rotpoint=None):
    (height,width)=img.shape[:2] # Get the height and width of the image

    if rotpoint is None:
        rotpoint=(width//2, height//2) # Set the rotation point to the center of the image
    # Create a rotation matrix      
    rotMat=cv.getRotationMatrix2D(rotpoint, angle, 1.0) # Get the rotation matrix
    # Apply the rotation to the image
    return cv.warpAffine(img, rotMat, (width, height)) # Apply the rotation to the image

rotatedimg=rotate(rescalingFrame(img), -45)  # Rotate the image by 45 degrees
cv.imshow('Rotated', rotatedimg)  # Display the rotated image

#flip
flippedimg=cv.flip(rescalingFrame(img), 0)  # Flip the image vertically
cv.imshow('Flipped', flippedimg)  # Display the flipped image

flippedimg2=cv.flip(rescalingFrame(img), 1)  # Flip the image horizontally
cv.imshow('Flipped2', flippedimg2)  # Display the flipped image  



cv.waitKey(0)  # Wait indefinitely for a key press