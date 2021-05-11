import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
import time

vs = VideoStream(src=1).start()
time.sleep(2.0)


while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=1000)
    # draw line
    # sidewalk position in px
    sw1 = 525 # 290cm from camera
    sw2 = 395 # 471 cm from camera
    frame = cv2.line(frame,(0,sw1),(1000,sw1),(255,0,0),2)
    frame = cv2.line(frame,(0,sw2),(1000,sw2),(255,0,0),2)
    # curb # 543 cm from camera
    cu1 = 365
    frame = cv2.line(frame,(0,cu1),(1000,cu1),(255,255,0),2)
    frame = cv2.line(frame, (500, 0), (500, 562),(255,255,0),1)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('t'):
        ret = cv2.imwrite('./road.jpg', frame)
        cv2.imshow('Frame2', frame)
        print(ret)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# vs.release()

# close all windows
# cv2.destroyAllWindows()

vs.stop()
cv2.destroyAllWindows()