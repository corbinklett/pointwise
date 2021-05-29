from collections import deque
import numpy as np
import argparse
import cv2
import time
import socket
import pickle
import localizer_params as param
import drawing_functions as drw
import measure_functions as meas
import comm_functions as comm

HEADERSIZE = 10 
IP = "127.0.0.1"
PORT = 1235
my_client_id = "sensor"

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", 
	help = "specify v for video feed or img file for static image.")
ap.add_argument("-v", "--verbose",
	help = "various functions will provide extra information.")
ap.add_argument("-c", "--connect", action = "store_true",
	help = "Connect to server and send data.")
args = vars(ap.parse_args())

if args['source'] == 'v':
	# get video stream
	cap = cv2.VideoCapture(0)
    # cap.set(4, 720)
else:
	img = args['source']
	frame = cv2.imread(img)

if args['connect'] == True:
	client_socket = comm.connect(IP, PORT, my_client_id)
	
	# test x-y coordinate
	test_data = np.array([1,2])
	comm.broadcast_data(test_data, client_socket)

	# gps coord of sensor
	comm.broadcast_data(param.sensor_gps, client_socket)

old_coord = meas.coord_clicked

while True:

	if args['source'] == 'v':
		ret, frame = cap.read()

	frame = cv2.resize(frame, (param.frame_width,param.frame_height), interpolation = cv2.INTER_AREA)

	frame = drw.draw_guidelines(frame)

	cv2.imshow('frame',frame)

	old_coord = meas.coord_clicked
	cv2.setMouseCallback('frame', meas.coordinate_click_event, frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		# save the last frame
		cv2.imwrite('./last_frame.jpg', frame)
		break

	# Broadcast data to server
	if meas.coord_clicked != old_coord:
		comm.broadcast_data(meas.coord_clicked, client_socket)

if args['source'] == 'v':
	cap.release()

cv2.destroyAllWindows()