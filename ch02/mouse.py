import sys
import numpy as np
import cv2


oldx = oldy = -1

# 마우스 이벤트 제어
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    # 마우스 이벤트 제어
    # cv2.EVENT_FLAG_CTRLKEY 이나 cv2.EVENT_MOUSEWHEEL
    # 마우스 좌표 체크
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    elif event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_RBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    # 마우스 이벤트시 입력
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 0, 0), 4, cv2.LINE_AA) # 라인을 그림 B G R
            cv2.imshow('image', img)
            oldx, oldy = x, y

        if flags & cv2.EVENT_FLAG_RBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 255, 255), 4, cv2.LINE_AA) # 라인을 그림 하얀색
            cv2.imshow('image', img)
            oldx, oldy = x, y


# 캔버스 사이즈
WIN_WIDTH = 1024
WIN_HEIGHT = 768
COLOR_CH = 3 # 트루컬러

# 비어있는 캔버스 생성, * 255(하얀색)
img = np.ones((WIN_WIDTH, WIN_HEIGHT, COLOR_CH), dtype=np.uint8) * 255

# 창 생성
cv2.namedWindow('image')
# 콜백 함수 : 마우스 이벤트를 계속 호출
cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
