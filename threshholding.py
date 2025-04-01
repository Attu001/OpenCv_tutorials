import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


cv.imread('./photos/bcat.jpg')
img1=cv.imread('./photos/bcat.jpg')
img=cv.resize(img1,(512,512)) #resize the image to 512x512 pixels

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #convert the image to grayscale
cv.imshow('Grayscale Image',gray) #show the grayscale image


#simple thresholding
threshold,thresh=cv.threshold(gray,127,255,cv.THRESH_BINARY) #apply simple thresholding
cv.imshow('Simple Thresholding',thresh) #show the thresholded image

#inverse thresholding
threshold,thresh_inv=cv.threshold(gray,127,255,cv.THRESH_BINARY_INV) #apply inverse thresholding
cv.imshow('Inverse Thresholding',thresh_inv) #show the thresholded images

#adapotive thresholding
threshold=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2) #apply adaptive thresholding
cv.imshow('Adaptive Thresholding',threshold) #show the thresholded image

cv.waitKey(0)
cv.destroyAllWindows()