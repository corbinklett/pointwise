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

HEADERSIZE = 10 
IP = "127.0.0.1"
PORT = 1234
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
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((IP, PORT))
	client_socket.setblocking(False)
	client_id = my_client_id.encode('utf-8')
	client_id_header = f"{len(my_client_id):<{HEADERSIZE}}".encode('utf-8')
	client_socket.send(client_id_header + client_id)
	
	# send map data
	# test x-y coordinate
	test_data = np.array([1,2])
	msg = pickle.dumps(test_data)
	print(len(msg))
	msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
	client_socket.send(msg)

	# broadcast static data
	# gps coord of sensor
	msg = pickle.dumps(param.sensor_gps)
	msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
	client_socket.send(msg)

	
while True:

	if args['source'] == 'v':
		ret, frame = cap.read()

	frame = cv2.resize(frame, (param.frame_width,param.frame_height), interpolation = cv2.INTER_AREA)

	frame = drw.draw_guidelines(frame)

	cv2.imshow('frame',frame)

	cv2.setMouseCallback('frame', meas.coordinate_click_event, frame)

	# Broadcast dynamic data here


	if cv2.waitKey(1) & 0xFF == ord('q'):
		# save the last frame
		cv2.imwrite('./last_frame.jpg', frame)
		break


if args['source'] == 'v':
	cap.release()

cv2.destroyAllWindows()