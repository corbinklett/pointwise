import cv2
import numpy as np

img = cv2.imread('road1.jpg')

ret = cv2.imshow('Road', img)
cv2.waitKey(0)
