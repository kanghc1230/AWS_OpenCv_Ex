import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

DEBUG = True

# 이미지 불러오기
img_path = "Hawkes.jpg"
src = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
if DEBUG == True:
    print(src.shape)

# 정상적으로 이미지를 불러왔는가
if src is None:
    print("failed to load image")
    sys.exit()

# src 히스토그램 띄우기
# calchist (리스트, 채널, 마스크, 히스토그램개수, range(0~255))
src_hist = cv2.calcHist([src], [0], None, [256], [0, 256])

# 히스토그램 평활화
dst = cv2.equalizeHist(src)

# dst 히스토그램 띄우기
dst_hist = cv2.calcHist([dst], [0], None, [256], [0, 256])

cv2.imshow("src",src)
cv2.imshow("dst",dst)

plt.plot(src_hist)
plt.show()
plt.plot(dst_hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
