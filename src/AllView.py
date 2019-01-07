import numpy as np
import cv2
font = cv2.FONT_HERSHEY_COMPLEX  # normal size serif font
cap = cv2.VideoCapture('videos\\car3.mp4')
ret, frame = cap.read()  # binary Video 객체
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))  #StructuringElement = 원본 media에 적용되는 kernel
gmgfgbg = cv2.bgsegm.createBackgroundSubtractorGMG() # gmg 전경객체
mogfgbg = cv2.bgsegm.createBackgroundSubtractorMOG() # mog 전경객체
mog2fgbg = cv2.createBackgroundSubtractorMOG2() # mog2 전경객체
while( ret ==1 ):
    #ret, frame = cap.read()  # binary Video 객체
    frame_re = cv2.resize(frame, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    fgmask = mogfgbg.apply(frame_re) # 전경 마스크 연산(프레임에)
    fgmask2 = mog2fgbg.apply(frame_re) # mog2 전경 마스크 연산
    fgmask3 = gmgfgbg.apply(frame_re) # gmg 전경 마스크 연산
    fgmask3 = cv2.morphologyEx(fgmask3, cv2.MORPH_OPEN, kernel) # gmg 모폴로지 연산
    cv2.putText(frame_re, 'Original', (230, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('ORIGINAL', frame_re)
    cv2.putText(fgmask, 'MOG', (290, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('MOG', fgmask) # mog 프레임
    cv2.putText(fgmask2, 'MOG2', (270, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('MOG2', fgmask2) # mog2 프레임
    cv2.putText(fgmask3, 'GMG', (290, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('GMG', fgmask3)  # gmg 프레임
    cv2.moveWindow('ORIGINAL', 50, 50)
    cv2.moveWindow('MOG', 440, 50)
    cv2.moveWindow('MOG2', 50, 300)
    cv2.moveWindow('GMG', 440, 300)
    ret, frame = cap.read()  # binary Video 객체
    k = cv2.waitKey(10) & 0xff
    if k == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
    elif k == ord('p'):
        while(1):
            wk = cv2.waitKey(0)
            if wk ==ord('p'):
                break
cap.release()
cv2.destroyAllWindows()