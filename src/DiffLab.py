import cv2
cap = cv2.VideoCapture("videos\\car3.mp4")
ret, current_frame = cap.read()
previous_frame = current_frame
font = cv2.FONT_HERSHEY_COMPLEX  # normal size serif font
while(ret ==1):
    current_frame_lab = cv2.cvtColor(current_frame, cv2.COLOR_BGR2LAB)
    previous_frame_lab = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2LAB)
    # 현재 프레임과 이전 프레임을 이진화하여 프레임별 grayFrame 객체생성(RGB to LAB COLOR)
    frame_diff = cv2.absdiff(current_frame_lab, previous_frame_lab)
    # 현재 프레임과 이전 프레임간의 차영상 확인
    frame_diff_re=cv2.resize(frame_diff, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    current_frame_re=cv2.resize(current_frame, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    #이미지 리사이징
    cv2.putText(current_frame_re, 'Original', (230,30), font, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.putText(frame_diff_re, 'CIALAB', (230,30), font, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.imshow('DIFF', frame_diff_re)
    cv2.imshow('ORIGINAL', current_frame_re)
    cv2.moveWindow('ORIGINAL', 100, 100)
    cv2.moveWindow('DIFF', 490, 100)
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
    # 현재프레임을 copy하여 이전 프레임 저장
    ret, current_frame = cap.read()
cap.release()
cv2.destroyAllWindows()