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
    keycode = cv2.waitKey() # 변수에 하나받아와서
    if keycode == ord('i') or keycode == ord('I'): # 아스키 i면
        img = ~img
        cv2.imshow('image', img)
    elif keycode == 27: # ESC면
        break

cv2.destroyAllWindows()
