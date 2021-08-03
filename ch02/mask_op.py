# 영상 합성
import sys
import cv2


# 마스크 영상을 이용한 영상 합성
src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE) #mask사진파일 그레이로
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

# 정상적으로 읽혔는지
if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

# src를 mask 씌운 부분만 dst로 보내기 #
cv2.copyTo(src, mask, dst)

# dst[mask > 0] = src[mask > 0]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()


# 알파 채널을 마스크 영상으로 이용
src = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)

if src is None or logo is None:
    print('Image load failed!')
    sys.exit()

# mask는 흑백형식 airplain
#print(logo.shape)  # (222, 180, 4)
mask = logo[:, :, 3]    # mask는 알파 채널로 만든 마스크 영상 0,1,2,3 # 로고를 흑백인 mask에 넣기
logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
h, w = mask.shape[:2]
print("mask_height :{0} , mask_weight :{1}".format(h,w))    # 222 180
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출 #10:10값은 로고의 위치가 바뀜

# logo를 mask 씌운 부분만 crop로 보내기 #
cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0]

cv2.imshow('src', src)      # 고양이+로고
cv2.imshow('logo', logo)    # 로고
cv2.imshow('mask', mask)    # 로고 마스크
cv2.waitKey()
cv2.destroyAllWindows()
