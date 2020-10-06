#!/usr/bin/env python3

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids): #zip joins two tuples/vector together into array pairs.
        return color

        #print(color) #rbg format
        

        # plot the relative percentage of each cluster
    #     endX = startX + (percent * 300)
    #     cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
    #                   color.astype("uint8").tolist(), -1)
    #     startX = endX

    # # return the bar chart
    # return bar




cap = cv2.VideoCapture(0)
height = int(cap.get(4))
width = int (cap.get(3))

while(1):   
    _, frame = cap.read() 
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    target_upper_left = (((width//2)-100),((height//2)-100))
    target_lower_right = (((width//2)+100),((height//2)+100))
    #print("left",target_upper_left,"right:", target_lower_right)
    target_box = cv2.rectangle(frame,target_upper_left,target_lower_right,(255,0,0),3)
    target_area = img[target_upper_left[1]:target_lower_right[1], target_upper_left[0]:target_lower_right[0]] #y1:y2,x1:x2 where y is lower_right, and x is upper left
    
    
    #cv2.imshow('target area', target_area) #inverted image?? but the color values are okay.
    #grab area to perform the kmeans process and reshape it
    #img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number
    target_area = target_area.reshape((target_area.shape[0] * target_area.shape[1],3))
    cluster_num = 1 #cluster number indicates what's the k dominant/majority colors in the image
    clt = KMeans(n_clusters=cluster_num) #cluster number
    #clt.fit(img)
    clt.fit(target_area)
    hist = find_histogram(clt)
    color = plot_colors2(hist, clt.cluster_centers_) #grab dominant color
    #bar = plot_colors2(hist, clt.cluster_centers_)

    

    #draw color in a box
    #print(color)

    bgr_color = (color[2], color[1], color[0])
    #bgr_color = (0,255,0)

    dom = np.zeros((height,width,3),np.uint8)
    dom = cv2.rectangle(dom,(0,0),(width,height),bgr_color,-1) #fill image with dominant color in bgr
    cv2.imshow('dominant color', dom)
    # plt.axis("off")
    # plt.imshow(bar)
    # plt.show()
    cv2.imshow("original",frame)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()