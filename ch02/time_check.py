import sys
import time
import numpy as np
import cv2
#사진읽기
img = cv2.imread('hongkong.jpg')

tm = cv2.TickMeter()

tm.reset()
tm.start() #시간시작
t1 = time.time()

# Canny 영상처리
edge = cv2.Canny(img, 50, 150)

tm.stop() #시간끝
print('time:', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))

