import numpy as np
import cv2


def on_level_change(pos):
    print("pos : {0}".format(pos))
    value = pos * 16
    if value >= 255:
        value = 255

    img[:] = value
    cv2.imshow('image', img)

# 검은색 캔버스 생성
img = np.zeros((480, 840), np.uint8)
# 'image' 창을 생성
cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
# 'image' 창 안에 trackbar 생성. ('level' 트랙바의 이름, 창이름,0,~16개, 움직일때마다 on_level_chang함수 작동)
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
