from collections import deque
import numpy as np
import argparse
import cv2
import time
import localizer_params as param
import drawing_functions as drw

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", 
	help = "specify v for video feed or img file for static image.")
args = vars(ap.parse_args())

if args['source'] == 'v':
	# get video stream
	cap = cv2.VideoCapture(0)
    # cap.set(4, 720)
else:
	img = args['source']
	frame = cv2.imread(img)
	


# set properties of frame
time.sleep(2.0)

while True:
	if args['source'] == 'v':
		ret, frame = cap.read()

	frame = cv2.resize(frame, (param.frame_width,param.frame_height), interpolation = cv2.INTER_AREA)

	frame = drw.draw_guidelines(frame)

	cv2.imshow('frame',frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		# save the last frame
		cv2.imwrite('./last_frame.jpg', frame)
		break


if args['source'] == 'v':
	cap.release()
	
cv2.destroyAllWindows()