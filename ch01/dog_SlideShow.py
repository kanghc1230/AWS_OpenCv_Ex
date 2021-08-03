# 화면을 4등분하여 시계방향으로 이미지가 슬라이드 하는 프로그램
import os
import sy s
import glob
import cv2 #
import numpy as np
# import matplotlib.pyplot as plt #창을 띄워서 처리
import win32api

def create_image_multiple(h, w, d, hcout, wcount):
    image = np.zeros((h*hcout, w*wcount,  d), np.uint8)
    color = tuple(reversed((0,0,0)))
    image[:] = color
    return image

def showMultiImage(dst, src, h, w, d, col, row):
    dst[(col*h):(col*h)+h, (row*w):(row*w)+w] = src[0:h, 0:w]
    # 0,1

img_path = 'C:/Users/BIT/OpencvEx/ch01/dog_image/*.jpg'
img_list = glob.glob(img_path)

if img_list is None:
    print("Failed to read img_list")
    sys.exit()

cv2.namedWindow("dog4Slide", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("dog4Slide", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

idx = 0
while True:
    img1 = cv2.imread(img_list[idx])
    img2 = cv2.imread(img_list[idx+1])
    img3 = cv2.imread(img_list[idx+2])
    img4 = cv2.imread(img_list[idx+3])

    idx += 4
    if idx >= len(img_list):
        idx = 0
    if img1 is None or img2 is None or img3 is None or img4 is None:
        print("Faild to load Image file")

    print(win32api.GetSystemMetrics(0) / 2)
    print(win32api.GetSystemMetrics(1) / 2)
    #print(img2.shpae[0])

    #창의 크기 set
    dogimageset = create_image_multiple(win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1), 3, 2, 2)

    height = img2.shape[0]
    width = img2.shape[1]
    depth = 3

    showMultiImage(dogimageset, img2, height, width, 3, 0, 0)
    showMultiImage(dogimageset, img2, height, width, 3, 0, 1)
    showMultiImage(dogimageset, img2, height, width, 3, 1, 0)
    showMultiImage(dogimageset, img2, height, width, 3, 1, 1)

    cv2.imshow('dog4Slide', dogimageset)

    # cv2.imshow("dog4Slide", img1)
    # cv2.imshow("dog4Slide", img2)
    # cv2.imshow("dog4Slide", img3)
    # cv2.imshow("dog4Slide", img4)
    if cv2.waitKey(1500) == 27:
        break

cv2.destroyAllWindows()