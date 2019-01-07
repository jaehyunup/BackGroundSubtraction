import numpy as np
# GMG 를 이용한 배경제거 시도
# Author : 박재현
import cv2
font = cv2.FONT_HERSHEY_COMPLEX  # normal size serif font
cap = cv2.VideoCapture('videos\\car3.mp4')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
while(1):
    ret, frame = cap.read()
    if ret == 1:
        frame = cv2.resize(frame, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        cv2.putText(frame, 'Original', (210, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(fgmask, 'GMG', (290, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('GMG',fgmask)
        cv2.imshow('ORIGINAL', frame)
        cv2.moveWindow('ORIGINAL', 100, 100)
        cv2.moveWindow('GMG', 500, 100)
        k = cv2.waitKey(1) & 0xff
        if k == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()