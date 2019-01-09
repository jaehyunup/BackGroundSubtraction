import numpy as np
import cv2 as cv2
font = cv2.FONT_HERSHEY_COMPLEX  # normal size serif font
cap = cv2.VideoCapture('videos\\car3.mp4')
fgbg = cv2.bgsegm.createBackgroundSubtractorLSBP()
# 배경 객체 생성
while(1):
    ret, frame = cap.read()
    if ret == 1:
        frame_re = cv2.resize(frame, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
        # binary 영상 객체
        fgmask = fgbg.apply(frame_re)
        bg=fgbg.getBackgroundImage()
        # 영상 객체에 6line 에서 생성된 전경마스크를 연산, 결과 영상은 fgmask
        cv2.putText(fgmask, 'GSOC', (280, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('GSOC', fgmask)
        # 전경 마스크 연산되어 배경 제거된 영상 출력
        cv2.putText(frame_re, 'Original', (230, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('ORIGINAL', frame_re)
        # 원본 영상 출력
        cv2.moveWindow('ORIGINAL',100,100)
        cv2.moveWindow('GSOC', 490, 100)

        k = cv2.waitKey(20) & 0xff
        if k == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
