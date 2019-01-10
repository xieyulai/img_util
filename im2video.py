#!/usr/bin/env python
import cv2

out = cv2.VideoWriter('yourvideo.avi',cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),25.0,(1294,720))

for i in reversed(range(51,892)):
        add = 'img/'+str(i)+'.jpg'
	print add
	img = cv2.imread(add)
        print add
        #cv2.imshow('detection',img)
        out.write(img)
out.release()
cv2.destroyAllWindows()



