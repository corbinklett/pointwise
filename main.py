from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video",
# 	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

vs = VideoStream(src=0).start()

# allow the camera or video file to warm up
time.sleep(2.0)

while True:
	frame = vs.read()

# relationship between pixel and distance
# what is the meters per pixel? mp = meters per pixel
# need to measure the lines and do a regression (polynomial?)
# to come up with relationship for x position and y position (a 2D polynomial fit)
dist = a*p**2

# encode lines
lane1 = 
line_x =np.array([x_low, x_high])