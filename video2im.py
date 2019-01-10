#!/usr/bin/env python
import cv2
video='yourvideo.avi'

cap = cv2.VideoCapture(video)

n = 1
if cap.isOpened == False:
    print "Fail to open video"
if cap.isOpened():
    while True:
        ret,img = cap.read()
        if ret == True:
	    if n%1 == 0:
            	cv2.imwrite('your_img_dir/'+str(n)+'.jpg',img)
            n=n+1
        else:
            break

cap.release()

