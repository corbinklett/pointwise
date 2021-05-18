import cv2
import localizer_params as param
import numpy as np

def get_coordinate(xp,yp):
    # xp, yp are the coordinates in pixels in the image frame 
    # (upper left corner of the image)

    vp = param.vanish_point

    # identify a line to apply cross-ratio to
    # p1 (beginning of sidewalk)
    # p2 (edge of sidewalk)

    # p3 (selected point)
    p3 = np.array((xp,yp))
  
    # p4 (vanishing point at infinity)
    p4 = np.array(vp)  

    delta_x = p3[0] - p4[0]
    delta_y = p3[1] - p4[1]
    hyp = np.sqrt(delta_x**2 + delta_y**2)

    # theta in [-pi/2, pi/2]
    cos_theta = delta_y / hyp
    sin_theta = delta_x / hyp
    tan_theta = delta_x / delta_y
    # print(np.arctan(tan_theta)*180/np.pi)

    # compute the ratio
    # the points are 
    P1 = 0
    P2 = 1.81 
    # P4 = infty

    # find pixel values (xp,yp) of p1 and p2
    p1_y = param.yp_sw_close
    p2_y = param.yp_sw_far

    p1_x = p4[0] + (p1_y - p4[1])*tan_theta
    p1 = np.array((p1_x,p1_y))
    p2_x = p4[0] + (p2_y - p4[1])*tan_theta
    p2 = np.array((p2_x,p2_y))

    # compute ratio
    d_p3p4 = np.linalg.norm(p3-p4)
    d_p1p4 = np.linalg.norm(p1-p4)
    d_p2p4 = np.linalg.norm(p2-p4)
    d_p1p2 = np.linalg.norm(p1-p2)
    d_p1p3 = np.linalg.norm(p1-p3)
    d_p2p3 = np.linalg.norm(p2-p3)

    d_P1P2 = 1.81

    # convert to real-world coordinates
    P2_Y = 4.71 # meters from camera

    # compute D, the distance from p2 to p3
    cross_ratio = (d_p1p3*d_p2p4)/(d_p2p3*d_p1p4)

    if p3[1] < param.yp_sw_far:
        D_P2P3 = d_P1P2/(cross_ratio - 1)
        P3_Y = cos_theta*D_P2P3 + P2_Y
    else:
        D_P2P3 = d_P1P2/(cross_ratio + 1) 
        P3_Y = P2_Y - cos_theta*D_P2P3
    
    print(P3_Y)
    # need to figure out x coordinate
    

def coordinate_click_event(event, x, y, flags, img):

    # x and y are in the xp-yp (image) frame

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:

        get_coordinate(x,y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('frame', img)





