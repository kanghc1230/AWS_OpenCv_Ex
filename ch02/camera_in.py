import sys
import cv2

filePath = 'C:/Users/kbg39/OpencvEx/ch02/video2.mp4'

# 카메라 열기 #USB를 꽂으면
cap = cv2.VideoCapture(filePath) #카메라 0 대신에 영상의 경로를 지정

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라(영상) 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 처리
while True:
    ret, frame = cap.read()
    rs_frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

    if not ret:
        break

    inversed = ~rs_frame  # 반전

    win_xpos = 40
    win_ypos = 30
    cv2.imshow('frame', rs_frame)
    cv2.imshow('inversed', inversed)
    cv2.moveWindow('rs_frame', win_xpos, win_ypos)
    cv2.moveWindow('inversed', win_xpos+(rs_frame.shape[1]), win_ypos) # int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #win_xpos+(rs_frame.shape[1])

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
