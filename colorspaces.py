import cv2 as cv
import matplotlib.pyplot as plt

resized=cv.resize(cv.imread('photos/bcat.jpg'), (500, 500))
cv.imshow('resized',resized)

# plt.imshow(resized)
# plt.show()


gray=cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

rgb=cv.cvtColor(resized, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

hsv=cv.cvtColor(resized, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

lab=cv.cvtColor(resized, cv.COLOR_BGR2Lab)
cv.imshow('Lab',lab)

cv.waitKey(0)
cv.destroyAllWindows()