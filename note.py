cv2.imread(), cv2.imshow() , cv2.imwrite()

cv2.imshow('window_name',img) can create different window names

cv2.waitKey(0)
cv2.destroyAllWindows()

to intially create window and specify size:
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

using matplotlib:
from matplotlib import pyplot as plt
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

Video capture:
cap = cv2.VideoCapture(0)
cap.get(some ID) # to get properties of video such as size

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

to write/save a video:
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

Drawing:
# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)