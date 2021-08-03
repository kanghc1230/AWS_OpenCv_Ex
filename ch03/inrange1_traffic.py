# 신호등이미지를 HSV와 RGB컬러로 비교하도록 색판별 코드를 완성하기 # 트랙바로 H,S , R,G,B 조절하고
import sys
import numpy as np
import cv2
Red = 0
Green = 0
Blue = 0

# 트랙바 pos 함수
def on_red_change(pos):
    global Red
    print("red : {0}".format(pos))
    Red = pos * 1
    if Red >= 255:
        Red = 255
    dst1 = cv2.inRange(src, (0, 128, 0), (Blue, Green, Red))  # BGR
    dst2 = cv2.inRange(src_hsv, (Red, Green, Blue), (80, 255, 255))  # hsv(색상 채도 명도) 50~80, 150~255, 0~255
    dst3 = cv2.inRange(src_rgb, (0, Green, 0), (Red, 255, Blue))  # RGB(RED GREEN BLUE) 녹색 0~100, 128~255 0~100 #128
    cv2.imshow('src_dst1', dst1)
    cv2.imshow('hsv_dst2', dst2)
    cv2.imshow('rgb_dst3', dst3)

def on_blue_change(pos):
    global Blue
    print("blue : {0}".format(pos))
    Blue = pos * 1
    if  Blue >= 255:
        Blue = 255
    dst1 = cv2.inRange(src, (0, 128, 0), (Blue, Green, Red))  # BGR
    dst2 = cv2.inRange(src_hsv, (Red, Green, Blue), (80, 255, 255))  # hsv(색상 채도 명도) 50~80, 150~255, 0~255
    dst3 = cv2.inRange(src_rgb, (0, Green, 0), (Red, 255, Blue))  # RGB(RED GREEN BLUE) 녹색 0~100, 128~255 0~100 #128
    cv2.imshow('src_dst1', dst1)
    cv2.imshow('hsv_dst2', dst2)
    cv2.imshow('rgb_dst3', dst3)

def on_green_change(pos):
    global Green
    print("green : {0}".format(pos))
    Green = pos * 1
    if Green >= 255:
        Green = 255
    # 추출 inRange(창 이름, (하한값), (상한값)
    dst1 = cv2.inRange(src, (0, 128, 0), (Blue, Green, Red)) #BGR(BLUE GREEN RED) 녹색추출 0~100, 128~255 0~100 #128
    dst2 = cv2.inRange(src_hsv, (Red, Green, Blue), (80, 255, 255)) #hsv(색상 채도 명도) 녹색추출 50~80, 150~255, 0~255
    dst3 = cv2.inRange(src_rgb, (0, Green, 0), (Red, 255, Blue)) #RGB(RED GREEN BLUE) 녹색추출 0~100, 128~255 0~100 #128
    # dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))  # BGR
    # dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))  # hsv(색상 채도 명도) 50~80, 150~255, 0~255
    # dst3 = cv2.inRange(src_rgb, (0, 128, 0), (100, 255, 100))  # RGB(RED GREEN BLUE) 녹색 0~100, 128~255 0~100 #128
    cv2.imshow('src_dst1', dst1)
    cv2.imshow('hsv_dst2', dst2)
    cv2.imshow('rgb_dst3', dst3)


# 파일 읽어오기
#src = cv2.imread('trafficLight1.jpg')
src = cv2.imread('trafficLight2.jpg')
#src = cv2.imread('trafficLight3.jpg')
#src = cv2.imread('candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()

# hsv, rgb
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
src_rgb = cv2.cvtColor(src_hsv, cv2.COLOR_HSV2RGB)

# 창 3개 생성
cv2.namedWindow('src',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('src_dst1',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('hsv_dst2',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('rgb_dst3',cv2.WINDOW_AUTOSIZE)

# 화면 띄우기 src는 그냥 나머진 on_level_change안에서
cv2.imshow('src', src)
cv2.createTrackbar('Red', 'src', 0, 255, on_red_change)  # 트렉바는 src창에만 생성. 계산은 함수로 묶여있음
cv2.createTrackbar('Green', 'src', 0, 255, on_green_change)
cv2.createTrackbar('Blue', 'src', 0, 255, on_blue_change)
cv2.waitKey()

cv2.destroyAllWindows()
