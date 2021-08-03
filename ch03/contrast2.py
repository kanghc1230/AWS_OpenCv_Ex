# 이미지 선명하게 만들기
import sys
import numpy as np
import cv2

# 파일 읽기
#src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# cliping
alpha = 1.0
dst1 = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)

# normalize
gmin, gmax, _, _ = cv2.minMaxLoc(src)
dst2 = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
#dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('clip_dst', dst1)
cv2.imshow('normal_dst', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
