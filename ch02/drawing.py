import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)

# 도형이나 직선을 그릴때는 점의 좌표는 모두 Tuple로
# 선을 그릴때    (처음좌표), (끝좌표), (B,G,R), 두께
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

# 사각형 그릴때       (처음좌표, X길이 Y길이), (B,G,R), 두께
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
# 사각형 그릴때       (처음좌표), (반대모서리좌표), (B,G,R), 두께
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1) # 두께가 -1이면 사각형 안을 채운다

# 원을 그릴때 (중심점), 반지름, (B,G,R), 두께, 라인스타일
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

# 다각형 그릴때 리스트로 좌표값
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
# cv2.polylines(창 , 좌표점, 선끼리연결 ,(B,G,R), 두께
cv2.polylines(img, [pts], True, (255, 0, 255), 3)
cv2.fillPoly(img, [pts], (255, 0, 0))

# 캔버스에 문자열을 추가할때
text = 'Hello? OpenCV ' + cv2.__version__
# 문자열 그리기 (창, 텍스트, 좌표, 폰트, 글씨크기,    (B,G,R), 두께, 라인스타일)
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
            (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

