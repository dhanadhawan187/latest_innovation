# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:23:28 2019

@author: SUDHARSAN SAMBATH
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = cv2.imread('f2.jpg')

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 1)
plt.imshow(img)
plt.show()
plt.imshow(th)
plt.show()
cv2.imwrite("D:/COLLEGE/SEM 6\PROJECTS/INNOVATION LAB/New folder/CODES/saved/adaptivethreshold2.jpg" , th) 
