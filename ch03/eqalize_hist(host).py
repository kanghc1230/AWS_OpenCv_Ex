#import

import sys
import matplotlib.pyplot as plt
import cv2
import numpy as np

DEBUG = True


def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist

#이미지를 불러오기
img_name = 'Hawkes.jpg'
src = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

# 정상적으로 이미지를 불러왔는가?
if src is None:
    print('Image load failed!')
    sys.exit()

if DEBUG==True:
    print(src.shape)

#히스토그램을 띄워보자.
# 입력영상 리스트, 채널, 마스크, 히스토그램 사이즈(bin), ranges(0~255)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)

#히스토그램 평활화

cv2.imshow('src_img',src)
cv2.imshow('src_hist',histImg)
cv2.waitKey(0)

cv2.destroyAllWindows()