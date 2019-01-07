# Frame Difference 를 이용한 배경제거 시도 ( HSV 변환 )
# Author : 박재현
import cv2
font = cv2.FONT_HERSHEY_COMPLEX  # normal size serif font

cap = cv2.VideoCapture("videos\\car3.mp4")
ret, current_frame = cap.read()
previous_frame = current_frame
while(ret ==1):
    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    previous_frame_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
    # 현재 프레임과 이전 프레임을 이진화하여 프레임별 grayFrame 객체생성
    # (RGB to GRAY)
    current_frame_lab = cv2.cvtColor(current_frame, cv2.COLOR_BGR2LAB)
    previous_frame_lab = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2LAB)
    # (RGB to LAB)
    current_frame_hls = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HLS)
    previous_frame_hls = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2HLS)
    # (RGB to HLS)
    current_frame_luv = cv2.cvtColor(current_frame, cv2.COLOR_BGR2LUV)
    previous_frame_luv = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2LUV)
    # (RGB to LUV)
    frame_diff_gray = cv2.absdiff(current_frame_gray, previous_frame_gray)
    frame_diff_lab = cv2.absdiff(current_frame_lab, previous_frame_lab)
    frame_diff_hls = cv2.absdiff(current_frame_hls, previous_frame_hls)
    frame_diff_luv = cv2.absdiff(current_frame_luv, previous_frame_luv)
    # 현재 프레임과 이전 프레임간의 차영상 확인

    current_frame_re = cv2.resize(current_frame, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    frame_diff_gray_re = cv2.resize(frame_diff_gray, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    frame_diff_lab_re = cv2.resize(frame_diff_lab, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    frame_diff_hls_re = cv2.resize(frame_diff_hls, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    frame_diff_luv_re = cv2.resize(frame_diff_luv, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    #이미지 리사이징
    cv2.putText(current_frame_re, 'ORIGINAL', (220,30), font, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.putText(frame_diff_gray_re, 'GRAY', (230,30), font, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.putText(frame_diff_lab_re, 'LAB', (230,30), font, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.putText(frame_diff_hls_re, 'HLS', (230,30), font, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.putText(frame_diff_luv_re, 'LUV', (230,30), font, 1, (255,255,255), 2, cv2.LINE_AA)
    # 텍스트 출력
    cv2.imshow('ORIGINAL', current_frame_re)
    cv2.imshow('GRAY', frame_diff_gray_re)
    cv2.imshow('LAB', frame_diff_lab_re)
    cv2.imshow('HLS', frame_diff_hls_re)
    cv2.imshow('LUV', frame_diff_luv_re)


    #출력
    cv2.moveWindow('ORIGINAL', 100, 100)
    cv2.moveWindow('GRAY', 490, 100)
    cv2.moveWindow('LAB', 100, 350)
    cv2.moveWindow('HLS', 490, 350)
    cv2.moveWindow('LUV', 100, 600)
    #화면 초기화

    k = cv2.waitKey(10) & 0xff
    if k == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
    elif k == ord('p'):
        while (1):
            wk = cv2.waitKey(0)
            if wk == ord('p'):
                break
    previous_frame = current_frame.copy()
    # 현재프레임을 copy하여 이전 프레임에 저장
    ret, current_frame = cap.read()
cap.release()
cv2.destroyAllWindows()