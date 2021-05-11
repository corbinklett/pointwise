import cv2
import numpy as np

cap = cv2.VideoCapture(1)
#cap.get(some ID) # to get properties of video such as size
width  = cap.get(3)  # float `width`
height = cap.get(4)
print(width)
print(height)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1000,562))

    # draw line
    # sidewalk position in px
    sw1 = 525 # 290cm from camera
    sw2 = 395 # 471 cm from camera
    frame = cv2.line(frame,(0,sw1),(1000,sw1),(255,0,0),2)
    frame = cv2.line(frame,(0,sw2),(1000,sw2),(255,0,0),2)
    # curb # 543 cm from camera
    cu1 = 365
    frame = cv2.line(frame,(0,cu1),(1000,cu1),(255,255,0),2)

    # Display the resulting frame
    cv2.imshow('Pointwise',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
