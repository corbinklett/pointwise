import cv2
import localizer_params as param

def draw_guidelines(img):

    # draw street lines using localizer_params.py
    #colors
    blue = (255,0,0)
    yellow = (255,255,0)

    # close sidewalk
    img = cv2.line(img,(0,param.yp_sw_close),(param.frame_width, param.yp_sw_close),blue,2)

    # far sidewalk
    img = cv2.line(img,(0,param.yp_sw_far),(param.frame_width,param.yp_sw_far),blue,2)

    # curb edge
    img = cv2.line(img,(0,param.yp_curb_edge),(param.frame_width,param.yp_curb_edge),blue,2)

    # parking line
    img = cv2.line(img,(0,param.yp_parking_line),(param.frame_width,param.yp_parking_line),yellow,2)

    # street center
    img = cv2.line(img,(0,param.yp_center_line),(param.frame_width,param.yp_center_line),yellow,2)

    # street far edge
    img = cv2.line(img,(0,param.yp_road_far),(param.frame_width,param.yp_road_far),yellow,2)

    # vertical center line
    img = cv2.line(img, (int(param.frame_width/2), 0), (int(param.frame_width/2), param.frame_height),blue,1)

    return img