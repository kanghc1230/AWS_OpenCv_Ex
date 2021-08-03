import numpy as np
import cv2

# 새 영상 생성하기
# empty 초기화x 쓰레기값
img1 = np.empty((240, 320), dtype=np.uint8)         # grayscale image
# 검은색이미지
img2 = np.zeros((240, 320, 3), dtype=np.uint8)      # color image
# 흰색 이미지 1* grey 255
img3 = np.ones((240, 320), dtype=np.uint8) * 255    # dark gray
# 노란색 이미지 모든 픽셀을 (0, 255, 255)로 채워라
img4 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)  # yellow

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()


# 영상 복사
img1 = cv2.imread('HappyFish.jpg')
# 얕은복사와 깊은복사
img2 = img1         # 얕은복사 주소값 같은것
img3 = img1.copy()  # 깊은복사 별개의것

img1.fill(255) #img1, img2 둘다 grey255 흰색으로

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 추출
img1 = cv2.imread('HappyFish.jpg')

img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱
img3 = img1[40:120, 30:150].copy()

img2.fill(0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()
