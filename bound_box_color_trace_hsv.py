#!/usr/bin/env python3

#Using HSV color scheme
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read() #is frame compatible with an image??

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue) #mask is a "grayscale" image

    #bound box processing
    contours,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for i in range(0, len(contours)):
    	if (i % 1 == 0):
    		cnt = contours[i]
    		x,y,w,h = cv2.boundingRect(cnt)
    		cv2.drawContours(mask ,contours, -1, (255,255,0), 3)
    		cv2.rectangle(mask,(x,y),(x+w,y+h),(255,0,0),2)
    		cv2.drawContours(frame ,contours, -1, (255,255,0), 3)
    		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    		

    cv2.imshow('frame',mask)
    cv2.imshow("original",frame)

    # # Bitwise-AND mask and original image
    # res = cv2.bitwise_and(frame,frame, mask= mask)

    # cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    # # cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

	
