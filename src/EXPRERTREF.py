import numpy as np
import cv2
font = cv2.FONT_HERSHEY_COMPLEX  # normal size serif font
cap = cv2.VideoCapture('videos\\car3'
                       '.mp4')
ret, frame = cap.read()  # binary Video 객체
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))  #StructuringElement = 원본 media에 적용되는 kernel
gmgfgbg = cv2.bgsegm.createBackgroundSubtractorGMG() # gmg 전경객체감산기
mogfgbg = cv2.bgsegm.createBackgroundSubtractorMOG() # mog 전경객체감산기
mog2fgbg = cv2.createBackgroundSubtractorMOG2() # mog2 전경객체감산기
gsoc = cv2.bgsegm.createBackgroundSubtractorGSOC() #gsoc 전경객체감산기
lsbp = cv2.bgsegm.createBackgroundSubtractorLSBP() # lsbp 전경객체감산기
cnt = cv2.bgsegm.createBackgroundSubtractorCNT() # cnt 전경객체감산기
while( ret ==1 ):
    frame_re = cv2.resize(frame, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    fgmask = mogfgbg.apply(frame_re) # 전경 마스크 연산(프레임에)
    fgmask2 = mog2fgbg.apply(frame_re) # mog2 전경 마스크 연산

    fgmask3 = gmgfgbg.apply(frame_re) # gmg 전경 마스크 연산
    fgmask3 = cv2.morphologyEx(fgmask3, cv2.MORPH_OPEN, kernel) # opening 연산 적용(GMG 특성상 노이즈가 많아서)

    fgmask4 = gsoc.apply(frame_re)
    fgmask5 = lsbp.apply(frame_re)
    fgmask6 = cnt.apply(frame_re)

    cv2.putText(frame_re, 'Original', (230, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('ORIGINAL', frame_re)
    cv2.putText(fgmask, 'MOG', (290, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('MOG', fgmask) # mog 프레임
    cv2.putText(fgmask2, 'MOG2', (270, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('MOG2', fgmask2) # mog2 프레임
    cv2.putText(fgmask3, 'GMG', (290, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('GMG', fgmask3)  # gmg 프레임
    cv2.putText(fgmask4, 'GSOC', (270, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('GSOC', fgmask4)  # GSOC
    cv2.putText(fgmask5, 'LSBP', (270, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('LSBP', fgmask5)  # LSBP
    cv2.putText(fgmask6, 'CNT', (270, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('CNT', fgmask6)  # LSBP

    cv2.moveWindow('ORIGINAL', 50, 10)
    cv2.moveWindow('MOG', 500, 10)
    cv2.moveWindow('MOG2', 50, 370)
    cv2.moveWindow('GMG', 500, 370)
    cv2.moveWindow('GSOC', 50, 740)
    cv2.moveWindow('LSBP', 500,740)
    cv2.moveWindow('CNT', 950, 10)

    ret, frame = cap.read()  # binary Video 객체
    k = cv2.waitKey(1) & 0xff
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