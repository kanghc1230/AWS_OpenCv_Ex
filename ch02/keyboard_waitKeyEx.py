import sys
import numpy as np
import cv2


img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    keycode = cv2.waitKeyEx() # 변수에 하나받아와서
    if keycode == 0x250000 or keycode == 0x260000: # ← ↑
        img = ~img
        cv2.imshow('image', img)
    elif keycode == 0x700000: # F1면
        break

cv2.destroyAllWindows()
