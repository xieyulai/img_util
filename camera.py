#!/usr/bin/env python
import cv2

cap = cv2.VideoCapture(2)
while 1:
    ret, frame = cap.read()
    cv2.imshow("cap", frame)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
