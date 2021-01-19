#!/usr/bin/env python
import cv2
import time

cap = cv2.VideoCapture(0)
Width = 1920
Height = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH,Width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,Height)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FPS,30)
#cap.set(3,1920)
#cap.set(4,1080)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
i = 0
while 1:
    t1 = time.time()
    ret, frame = cap.read()
    t2 = time.time()
    t = t2-t1
    #print(1/t)
    cv2.imshow("cap", frame)
    cv2.imwrite('img/{}.jpg'.format(i),frame)
    i += 1
    if cv2.waitKey(100) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
