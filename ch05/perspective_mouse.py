import sys
import numpy as np
import cv2


pt1 = [0,0]
pt2 = [0,0]
pt3 = [0,0]
pt4 = [0,0]
counter = 0

def on_mouse (event, x, y, flags, param):
    global counter , pt1, pt2, pt3, pt4
    if flags & cv2.EVENT_FLAG_LBUTTON:
        # counter값번째 순서 pt
        if counter == 0:
            pt1 = [x,y]
            print("pt1 x: {}, y: {}".format(x, y))
        elif counter == 1:
            pt2 = [x,y]
            print("pt2 x: {}, y: {}".format(x, y))
        elif counter == 2:
            pt3 = [x,y]
            print("pt3 x: {}, y: {}".format(x, y))
        elif counter == 3:
            pt4= [x,y]
            print("pt4 x: {}, y: {}".format(x, y))
        counter += 1

    # 취소
    elif flags & cv2.EVENT_FLAG_RBUTTON:
        if counter > 0:
            counter -= 1
            print (counter)
    #if event == cv2.EVENT_MOUSEMOVE:
        # print("x: {}, y: {}".format(x,y))


# 파일 읽기
src = cv2.imread('namecard.jpg')
# 'namecard.jpg' 'remo.jpg' 'load.jpg' 'face.jpg'

if src is None:
    print('Image load failed!')
    sys.exit()

# src 창 생성
cv2.namedWindow('src')
# 창에서 마우스의 이벤트가 감지되면 on_mouse메소드가 호출
cv2.setMouseCallback('src', on_mouse, src)

cv2.imshow('src', src)

# 마우스 좌표값이 모두 입력되고 아무키 키입력으로 진행
cv2.waitKey()

#이미지 좌표위치
w, h = 720, 400

# srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32)
# 시계방향으로마우스 좌표지정
srcQuad = np.array([pt1, pt2, pt3, pt4], np.float32)
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
