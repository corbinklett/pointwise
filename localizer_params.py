# frame parameters
frame_height = 562 # pixels
frame_width = 1000 # pixels

# sidewalk coordinates in xp-yp frame, as percentage of image height
yp_sw_close_pct = 525/562
yp_sw_far_pct = 395/562
yp_curb_edge_pct = 365/562
yp_parking_line_pct = 300/562
yp_center_line_pct = 250/562
yp_road_far_pct = 150/562

# actual coord in pixels in xp-yp frame
yp_sw_close = int(yp_sw_close_pct*frame_height)
yp_sw_far = int(yp_sw_far_pct*frame_height)
yp_curb_edge = int(yp_curb_edge_pct*frame_height)
yp_parking_line = int(yp_parking_line_pct*frame_height)
yp_center_line = int(yp_center_line_pct*frame_height)
yp_road_far = int(yp_road_far_pct*frame_height)

# vanishing point
vanish_point = (300,20)
