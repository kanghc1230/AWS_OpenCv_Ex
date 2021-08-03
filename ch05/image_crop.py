# Import packages
import cv2
import numpy as np

img = cv2.imread('road.jpg') # 412 x 799
# print(img.shape) # Print image shape
img_width = img.shape[1]
img_height = img.shape[0]

#412중에서 2/3부분 799
crop_pos_y = (img_height // 3) * 2
crop_pos_x = img_height

cv2.imshow("original", img)

# Cropping an image
# 앞에 값이 [height범위 H:H , wdith w:w]
cropped_image = img[crop_pos_y:img_height-1, 200:img_width-100]
#cropped_image = img[80:280, 150:330]

# Display cropped image
cv2.imshow("cropped", cropped_image)

# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()