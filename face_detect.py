import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img=cv.resize(cv.imread('./photos/faces.jpg'),(512,512)) #resize the image to 512x512 pixels

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #convert the image to grayscale
cv.imshow('Grayscale Image',gray) #show the grayscale image

haar_casade=cv.CascadeClassifier('haar_face.xml') #load the haar cascade classifier for face detection
face_rects=haar_casade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4) #detect faces in the image
print(len(face_rects)) #print the coordinates of the detected faces

for (x,y,w,h) in face_rects:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) #draw rectangles around the detected faces


cv.imshow('Detected Faces',img) #show the image with detected faces


cv.waitKey(0) #wait for a key press
cv.destroyAllWindows() #close all windows