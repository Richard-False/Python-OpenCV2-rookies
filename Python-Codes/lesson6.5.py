import cv2
import numpy as np
image_color=cv2.imread(r'C:\Users\pc\Desktop\picture1.jpg',cv2.IMREAD_COLOR)
mask = np.zeros_like(image_color)
# 定义一个ROI
mask[100:150, 100:150] = 255
result = cv2.bitwise_and(image_color, image_color, mask=mask)
cv2.imshow('Image Window1',result)
cv2.waitKey(10000)
cv2.destoryAllWindows()
