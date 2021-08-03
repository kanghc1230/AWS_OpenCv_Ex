import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)

# 다각형 그릴때 리스트로 좌표값
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
# cv2.polylines(창 , 좌표점, 선끼리연결 ,(B,G,R), 두께
cv2.polylines(img, [pts], True, (255, 0, 255), 3)
cv2.fillPoly(img, [pts], (255, 0, 0))

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

