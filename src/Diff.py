# Frame Difference 를 이용한 배경제거 시도 ( GRAY 변환 )
# Author : 박재현
import cv2
cap = cv2.VideoCapture("videos\\car2.mp4")
ret, current_frame = cap.read()
previous_frame = current_frame

while(ret == 1):

    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    previous_frame_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
    # 현재 프레임과 이전 프레임을 이진화하여 프레임별 grayFrame 객체생성
    frame_diff = cv2.absdiff(current_frame_gray, previous_frame_gray)
    # 현재 프레임과 이전 프레임간의 차영상 확인

    cv2.imshow('DIFF', frame_diff)
    cv2.imshow('ORIGINAL', current_frame)
    cv2.moveWindow('ORIGINAL', 100, 100)
    cv2.moveWindow('DIFF', 900, 100)

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