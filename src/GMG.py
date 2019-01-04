import numpy as np
import cv2 as cv2
cap = cv2.VideoCapture('vtest.avi')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
while(1):
    ret, frame = cap.read()
    if ret == 1:
        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(1) & 0xff
        if k == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()