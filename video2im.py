#!/usr/bin/env python
import cv2
video='1080-2.avi'

cap = cv2.VideoCapture(video)

n = 1
if cap.isOpened == False:
    print "Fail to open video"
if cap.isOpened():
    while True:
        ret,prev = cap.read()
        if ret == True:
	    if n%1 == 0:
            	cv2.imwrite('img_new/'+str(n)+'.jpg',prev)
            n=n+1
        else:
            break

cap.release()

