import cv2 as cv 
import numpy as np

cv.imread('photos/bcat.jpg')
resized=cv.resize(cv.imread('photos/bcat.jpg'), (500, 500))

blank=  np.zeros(resized.shape[:2], dtype='uint8')
cv.imshow('blank',blank)

mask=cv.circle(blank, (resized.shape[1]//2, resized.shape[0]//2), 100, 255, -1)
cv.imshow('mask',mask)

masked=cv.bitwise_and(resized, resized, mask=mask)
cv.imshow('masked',masked)

#intersection
maskint=cv.circle(blank, (resized.shape[1]//2, resized.shape[0]//2), 100, 255, -1)
cv.imshow('maskint',maskint)

cv.waitKey(0)
cv.destroyAllWindows()