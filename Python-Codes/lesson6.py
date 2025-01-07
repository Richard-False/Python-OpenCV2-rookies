import cv2
import numpy as np
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))


x = np.uint8([10])
y = np.uint8([250])
print(cv2.subtract(x, y))


# 图像权重相加示例
img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')
result = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
