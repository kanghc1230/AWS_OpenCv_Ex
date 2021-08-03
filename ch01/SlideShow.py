import sys
import glob
import cv2
import os

# 이미지 파일을 모두 img_files 리스트에 추가
img_path = 'C:/Users/kbg39/OpencvEx/ch01/images/*.jpg'
img_files = glob.glob(img_path) #glob와 os.listdir
#img_files2 = os.listdir('\\imaage\\*)

if not img_files:
    print("There are no jpg files in 'images' folder")
    sys.exit()

# 전체 화면으로 'image' 창 생성
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 무한 루프
cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print('Image load failed!')
        break

    cv2.imshow('image', img) #화면띄우기
    if cv2.waitKey(1000) >= 0: #종료키
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()
