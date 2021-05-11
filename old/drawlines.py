import cv2
import numpy as np
import measure_functions.py

def click_event(event, x, y, flags, params):
  
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
  
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('frame', img)

        # draw line
        # sidewalk position in px
        sw1 = 525 # 290cm from camera
        sw2 = 395 # 471 cm from camera
        # curb # 543 cm from camera
        cu1 = 365

        # select points using mouse
        # identify a line to apply cross-ratio to
        # p1 (beginning of sidewalk, sw1)
        # p2 (edge of sidewalk)
        # p3 (selected point)
        # p4 (vanishing point at infinity)
        vp = (500, 0) #(xv, yv) in the picture coordinate system
        p4 = np.array(vp)
        # pick point p3
        p3 = np.array((x,y))

        delta_x = p3[0] - p4[0]
        delta_y = p3[1] - p4[1]
        hyp = np.sqrt(delta_x**2 + delta_y**2)
        cos_theta = delta_y / hyp
        sin_theta = delta_x / hyp
        tan_theta = delta_x / delta_y
        print("dx: " + str(delta_x))
        print("dy: " + str(delta_y))
        print("hyp: " + str(hyp))
        print(cos_theta)
        print(np.arccos(cos_theta))

        # compute the ratio
        # the points are 
        P1 = 0
        P2 = 1.81 
        # P4 = infty

        # find pixel values (xp,yp) of p1 and p2
        p1_y = sw1
        p2_y = sw2

        p1_x = p4[0] - tan_theta*(p4[1] - p1_y)
        p1 = np.array((p1_x,p1_y))
        p2_x = p4[0] - tan_theta*(p4[1] - p2_y)
        p2 = np.array((p2_x,p2_y))

        # compute ratio
        d_p3p4 = np.linalg.norm(p3-p4)
        d_p1p4 = np.linalg.norm(p1-p4)
        d_p2p4 = np.linalg.norm(p2-p4)
        d_p1p2 = np.linalg.norm(p1-p2)
        d_p1p3 = np.linalg.norm(p1-p3)
        d_p2p3 = np.linalg.norm(p2-p3)

        d_P1P2 = 1.81

        # compute D, the distance from p2 to p3
        cross_ratio = (d_p1p3*d_p2p4)/(d_p2p3*d_p1p4)
        D_P2P3 = d_P1P2/(cross_ratio - 1)

        # convert to real-world coordinates
        P2_Y = 4.71 # meters from camera
        # P2_X = 
        P3_Y = cos_theta*D_P2P3 + P2_Y
        print(P3_Y)

        # need to label p1_x points by measuring 




img = cv2.imread('road2.jpg')
height, width, channels = img.shape
print(height)
print(width)
# get image size: 562 height x 1000 width

# draw line
# sidewalk position in px
sw1 = 525 # 290cm from camera
sw2 = 395 # 471 cm from camera
img = cv2.line(img,(0,sw1),(1000,sw1),(255,0,0),2)
img = cv2.line(img,(0,sw2),(1000,sw2),(255,0,0),2)
# curb # 543 cm from camera
cu1 = 365
img = cv2.line(img,(0,cu1),(1000,cu1),(255,255,0),2)

img = cv2.line(img, (int(width/2), 0), (int(width/2), height),(255,255,0),1)


while True:
    cv2.imshow('frame', img)
    #cv2.imshow('frame2', imgtran)

    cv2.setMouseCallback('frame', click_event)

    cv2.waitKey(0)
    break

cv2.destroyAllWindows()