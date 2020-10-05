#!/usr/bin/env python3
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
red = np.uint8([[[0,0,255]]])
hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
print(hsv_red)

while(1):

    # Take each frame
    _, frame = cap.read()
    red = np.uint8([[[255,0,0]]])
    # Convert BGR to HSV
    hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_red = np.array([-10,100,100])
    upper_red = np.array([10,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()