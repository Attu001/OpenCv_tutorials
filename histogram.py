import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('./photos/bcat.jpg')

resize=cv.resize(img,(512,512)) #resize the image to 512x512 pixels

cv.imshow('Resized Image',resize) #show the resized image

gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY) #convert the image to grayscale
cv.imshow('Grayscale Image',gray) #show the grayscale image

#grayscale histogram
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256]) #calculate the histogram of the grayscale image
cv.imshow('Grayscale Histogram',gray_hist) #show the histogram

plt.figure() #create a new figure
plt.title('Grayscale Histogram') #set the title of the figure
plt.xlabel('Pixel Value') #set the x-axis label
plt.ylabel('Frequency') #set the y-axis label
plt.plot(gray_hist) #plot the histogram
plt.xlim([0,256]) #set the x-axis limits
plt.ylim([0,5000]) #set the y-axis limits
plt.show() #show the plot

cv.waitKey(0)
#