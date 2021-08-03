import sys
import numpy as np
import cv2

src = cv2.imread('namecard.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

# src 창 생성
cv2.namedWindow('src')

w, h = 720, 400
#이미지 좌표위치
srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32) #결과값 좌표위치

# per는 변환행렬 (3x3 matrix)
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h))

while True:
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    keyValue = cv2.waitKey()
    if keyValue == 27:
        break
cv2.destroyAllWindows()
