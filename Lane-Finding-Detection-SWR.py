# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 19:33:23 2018
@author: Administrator
"""
def Canny_Edge_Detector(line_image):
    image= np.copy(line_image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)
    Ratio = 3
    low_threshold = 50
    high_threshold = low_threshold*Ratio # 1:3 Threshold Ratio 
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    return edges

def Hough_Space(image):
    masked_edges = Canny_Edge_Detector(image)
    rho = 1
    theta = np.pi/180
    threshold = 50       # increase number of inersection point to represent Line 
    min_line_length = 10
    max_line_gap = 20    # increase Max Gap 
    line_image = np.copy(image)*0 #creating a blank to draw lines on
    lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    #color_edges = np.dstack((masked_edges, masked_edges, masked_edges)) # X , Y , Z and convert to Binary Color 
    #combo = cv2.addWeighted(color_edges, .8, line_image, 1, 0)
    return line_image

def RegionMask(image):
    ROI = np.copy(image)*0 #creating a blank to draw lines on
    ysize = image.shape[0]
    xsize = image.shape[1]
    left_bottom = [100, 540]
    right_bottom = [920, 540]
    apex = [480, 320]
    fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
    fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
    fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)
    # Find the region inside the lines
    XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
    region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))
    ROI[region_thresholds] = [255,0,0]
   # plt.imshow(ROI)
    #plt.show()
    return ROI  
#******************************************************************Start Main Code
#doing all the relevant imports
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import numpy as np
import cv2

cap = cv2.VideoCapture('solidWhiteRight.mp4')

while(1):
    ret ,frame = cap.read()
    if ret == True:
        # git Hough Space
        Lines_Draw = Hough_Space(frame)
        #git roi 
        ROI=RegionMask(frame)
        result = cv2.bitwise_and(ROI,Lines_Draw)
        OUT = cv2.addWeighted(frame, 1, result, 1, 0)
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            cv2.imshow('result',result)
            cv2.imshow('frame',OUT)
    else:
        print('Error Vedio')
        break
cv2.destroyAllWindows()
cap.release()
    
    