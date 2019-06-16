#!/usr/bin/env python
#
#
import numpy as np
import cv2

img = np.zeros((200,320,3), dtype="uint8")

for x in range(0, 320):
    for y in range(0, 200):
        th = np.arctan2(y-100, x-160)
        r = ((y-100)**2 + (x-160)**2)**0.5 * 0.5
        v_b = 128 + int(r * np.cos(th))
        v_r = 128 + int(r * np.cos(th-np.pi*2.0/3.0))
        v_g = 128 + int(r * np.cos(th-np.pi*4.0/3.0))
        img[y, x, :] =  [v_b, v_r, v_g]
        print('(%3.0f %3.0f %3.0f) (th=%f  r=%f)' % (img[y,x,0], img[y,x,1], img[y,x,2], th, r))


txt_disp = "Hello, World"
txt_size, txt_bl = cv2.getTextSize(txt_disp, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontScale=1.0, thickness=1)
print("txt_size:(%d,%d)  txt_bl:%d" % (txt_size + (txt_bl,)))
cv2.putText(img, text='Hello, World', 
        org=(160-txt_size[0]/2, 100-txt_size[1]/2),
        fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX|cv2.FONT_ITALIC,
        fontScale=1.0, color=[0,255,255])

cv2.imshow('Color Disk', img)
cv2.waitKey(0)


