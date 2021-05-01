import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
import time


vs = VideoStream(src=2).start()
time.sleep(2.0)


while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=1000)

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