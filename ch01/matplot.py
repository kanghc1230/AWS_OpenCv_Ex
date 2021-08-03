#3번실행하는 프로그램
import sys
import matplotlib.pyplot as plt
import cv2 #  cv2 에러 https://lee-mandu.tistory.com/517?category=838684 미니콘다 설정방법
import glob

#image_path = 'C:/Users/kbg39/OpencvEx/ch01/cat.bmp'
imageList = glob.glob('C:/Users/kbg39/OpencvEx/ch01/*.bmp')
#imageList = glob.glob('C:/Users/BIT/OpencvEx/ch01/cat.bmp') #학원에선 BIT

# 컬러 영상 출력
#imgBGR = cv2.imread('cat.bmp') #BGR
imgBGR = cv2.imread(imageList[0])
#BGR그냥뿌리면 파란색 계열로 나옴. 이유는 openCV는 BGR로 사용하지만, Matplotlib는 RGB로 이미지를 보여주기 때문?
if imgBGR is None:
    print("Image load failed")
    sys.exit()

imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) #RGB로 cvt

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
