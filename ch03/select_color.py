''' task 신호등 이미지 색상추출
HSV와 RGB 컬러 스페이스로 비교해보고 색을 판별
1.트랙바 활용
    hsv, rgb 3개
2. cvtColor(bgr2hsv)
'''
import numpy as np
import cv2
import sys

DEBUG = True
img_path = 'C:/Users/kbg39/OpencvEx/ch03/trafficLight1.jpg'

IMG_HEIGHT = 340
IMG_WIDTH = 640
Hmin = 0
Hmax = 179
Smin = 0
Smin = 255
Vmin = 0
Vmax = 255


def on_Hmin_change(pos):
    global Hmin
    global Hmax
    Hmin = pos
    if Hmax < pos:
        cv2.setTrackbarPos("Hmin", 'image', Hmax-1) #hmin이 hmax-1보다 더못높이게
        Hmin = Hmax - 1

    if DEBUG == True:
        print("Hmin = {}".format(Hmin))

def on_Hmax_change(pos):
    global Hmin
    global Hmax
    Hmax = pos
    if Hmin > pos:
        cv2.setTrackbarPos("Hmax", 'image', Hmin + 1)
        Hmax = Hmin + 1

    if DEBUG == True:
        print("Hmax = {}".format(Hmax))

def on_Smin_change(pos):
    global Smin
    global Smax
    Smin = pos
    if Smax < pos:
        cv2.setTrackbarPos("Smin", 'image', Smax - 1)
        Smin = Smax - 1

    if DEBUG == True:
        print("Smin = {}".format(Smin))

def on_Smax_change(pos):
    global Smin
    global Smax
    Smax = pos
    if Smin > pos:
        cv2.setTrackbarPos("Smax", 'image', Smin + 1)
        Smax = Smin + 1

    if DEBUG == True:
        print("Smax = {}".format(Smax))

def on_Vmin_change(pos):
    global Vmin
    global Vmax
    Vmin = pos
    if Vmax < pos:
        cv2.setTrackbarPos("Vmin", 'image', Vmax - 1)
        Vmin = Vmax - 1

    if DEBUG == True:
        print("Vmin = {}".format(Vmin))

def on_Vmax_change(pos):
    global Vmin
    global Vmax
    Vmax = pos
    if Vmin > pos:
        cv2.setTrackbarPos("Vmax", 'image', Vmin + 1)
        Vmax = Vmin + 1
    # else:
    #     cv2.setTrackbarPos("Vmax", 'image', Vmax)

    if DEBUG == True:
        print("Vmax = {}".format(Vmax))


# 비어있는 캔버스 생성
img = np.zeros((IMG_HEIGHT, IMG_WIDTH, 3), np.uint8)
print(img.shape)

# 소스 이미지파일
src = cv2.imread(img_path)
if src is None:
    print('Image load failed!')
    sys.exit()

hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)


# 창을 생성 (창이름, 형식)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', IMG_WIDTH, IMG_HEIGHT)

cv2.namedWindow('src',cv2.WINDOW_NORMAL)
cv2.resizeWindow('src', IMG_WIDTH, IMG_HEIGHT)

cv2.namedWindow('hsv',cv2.WINDOW_NORMAL)
cv2.resizeWindow('hsv', IMG_WIDTH, IMG_HEIGHT)

cv2.namedWindow('rgb',cv2.WINDOW_NORMAL)
cv2.resizeWindow('rgb', IMG_WIDTH, IMG_HEIGHT)


# 트랙바 추가
cv2.createTrackbar('Hmin', 'image', 0, 179, on_Hmin_change)
cv2.createTrackbar('Hmax', 'image', 0, 179, on_Hmax_change)
cv2.createTrackbar('Smin', 'image', 0, 255, on_Smin_change)
cv2.createTrackbar('Smax', 'image', 0, 255, on_Smax_change)
cv2.createTrackbar('Vmin', 'image', 0, 255, on_Vmin_change)
cv2.createTrackbar('Vmax', 'image', 0, 255, on_Vmax_change)

# 여기에 txt파일을 읽어와서 작동하고 자동으로 마지막값을 저장해주는 코드
# Todo

# 트랙바 위치를 원하는값으로 설정할때 쓰는함수 (지금은 초기값처럼)
cv2.setTrackbarPos("Hmin", 'image', 0)
cv2.setTrackbarPos("Hmax", 'image', 179)
cv2.setTrackbarPos("Smin", 'image', 0)
cv2.setTrackbarPos("Smax", 'image', 255)
cv2.setTrackbarPos("Vmin", 'image', 0)
cv2.setTrackbarPos("Vmax", 'image', 255)

cv2.imshow('image', img)
cv2.imshow('src', src)

while True:
    # 붉은색은 0~30과
    mask1 = cv2.inRange(hsv, (0,135,202), (30,255,255))
    mask2 = cv2.inRange(hsv, (160, 135, 202), (179, 255, 255))
    redmask = cv2.add(mask1,mask2)
    # 마스크를 만들어주는 inRange. 색을 벗어나는값 (ex빨강,파랑)은 검정으로 제외
    hsv_msk = cv2.inRange(hsv, (Hmin, Smin, Vmin), (Hmax, Smax, Vmax))
    rgb_msk = cv2.inRange(rgb, (Hmin, Smin, Vmin), (Hmax, Smax, Vmax))
    cv2.imshow('redmask', redmask)
    cv2.imshow('hsv', hsv_msk)
    cv2.imshow('rgb', rgb_msk)
    if cv2.waitKey(200)==27:
        break

cv2.destroyAllWindows()