import numpy as np
import cv2 as cv2
cap = cv2.VideoCapture('vtest.avi')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  #StructuringElement = 원본 media에 적용되는 kernel
gmgfgbg = cv2.bgsegm.createBackgroundSubtractorGMG() # gmg 전경객체
mogfgbg = cv2.bgsegm.createBackgroundSubtractorMOG() # mog 전경객체
mog2fgbg = cv2.createBackgroundSubtractorMOG2() # mog2 전경객체

while(1):
    ret, frame = cap.read() # binary Video 객체
    if ret == 1:
        frame_re = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        fgmask = mogfgbg.apply(frame_re) # 전경 마스크 연산(프레임에)
        fgmask2 = mog2fgbg.apply(frame_re) # mog2 전경 마스크 연산
        fgmask3 = gmgfgbg.apply(frame_re) # gmg 전경 마스크 연산
        fgmask3 = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel) # gmg 모폴로지 연산


        cv2.imshow('ORIGINAL', frame_re)
        cv2.imshow('MOG', fgmask) # mog 프레임
        cv2.imshow('MOG2', fgmask2) # mog2 프레임
        cv2.imshow('GMG', fgmask3)  # gmg 프레임

        cv2.moveWindow('ORIGINAL', 50, 50)
        cv2.moveWindow('MOG', 440, 50)
        cv2.moveWindow('MOG2', 50, 380)
        cv2.moveWindow('GMG', 440, 380)

        k = cv2.waitKey(20) & 0xff
        if k == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()