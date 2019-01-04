import numpy as np
import cv2 as cv2

cap = cv2.VideoCapture('vtest.avi')
# 원본 비디오 객체
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
# 배경 객체 생성
while(1):
    ret, frame = cap.read()
    if ret == 1:
        frame_re = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        # binary 영상 객체
        fgmask = fgbg.apply(frame_re)
        # 영상 객체에 6line 에서 생성된 전경마스크를 연산, 결과 영상은 fgmask
        cv2.imshow('MOG', fgmask)
        # 전경 마스크 연산되어 배경 제거된 영상 출력
        cv2.imshow('ORIGINAL', frame_re)
        # 원본 영상 출력
        cv2.moveWindow('ORIGINAL',100,100)
        cv2.moveWindow('MOG', 500, 100)

        k = cv2.waitKey(1) & 0xff
        if k == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

