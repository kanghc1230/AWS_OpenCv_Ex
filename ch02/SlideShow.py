import glob # 파읽 읽어들이기
import os   # path
import cv2  # opencv
import sys  # sys.exit()

interval = 1500 #1.5sec

# 파일 경로설정 / or \\
#print (os.sep)
# img_path ='C:/Users/취업지원팀/OpencvEx/ch01/images/*.jpg' # 한글경로는 읽을수없음
# print(img_path)
# 방법2
base_path = 'C:\\Users\\BIT\\OpencvEx\\'
img_path = os.path.join(base_path, 'ch01\\images\\*.jpg')
# print(img_path)

# 이미지 파일명 리스트 읽어들이기
img_list = glob.glob(img_path)
print(img_list)

# 리스트에 이미지 파일명들을 정상적으로 읽어들이지 못했을경우
if img_list is None:
    print("img_list : no jpg files")
    sys.exit()

# 이미지 출력할 창을 생성
cv2.namedWindow("slideFrame", cv2.WINDOW_NORMAL)
# 이미지 출력할 창의 크기를 풀스크린으로
cv2.setWindowProperty("slideFrame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 이미지 읽어들이기
index = 0
while True:
    img = cv2.imread(img_list[index])

    # 이미지를 읽지 못했다면
    if img is None:
        print("image load failed")
        break

    cv2.imshow('slideFrame',img)
    # ESC입력을 들어올떄까지 슬라이드 진행
    if cv2.waitKey(interval) == 27:
        break

    # 슬라이드 반복
    index += 1
    if index >= len(img_list):
        index = 0

# 모든창 종료
cv2.destroyAllWindows()
# 개별적인 창 종료 cv2.destroyWindow("창이름")
#cv2.destroyWindow("slideFrame")