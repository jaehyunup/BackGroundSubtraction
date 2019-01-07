import cv2
font = cv2.FONT_HERSHEY_COMPLEX  # normal size serif font
cap = cv2.VideoCapture("videos\\car3.mp4")
ret, current_frame = cap.read()
previous_frame = current_frame
while(ret ==1):
    current_frame_hls = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HLS)
    previous_frame_hls = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2HLS)
    # 현재 프레임과 이전 프레임을 이진화하여 프레임별 grayFrame 객체생성
    frame_diff = cv2.absdiff(current_frame_hls, previous_frame_hls)
    # 현재 프레임과 이전 프레임간의 차영상 확인
    frame_diff_re=cv2.resize(frame_diff, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    current_frame_re=cv2.resize(current_frame, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    #이미지 리사이징
    cv2.putText(current_frame_re, 'Original', (230, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame_diff_re, 'HLS', (230, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
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
    # 현재프레임을 copy하여 이전 프레임에 저장
    ret, current_frame = cap.read()
cap.release()
cv2.destroyAllWindows()