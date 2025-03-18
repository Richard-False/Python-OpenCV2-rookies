import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread(r'picture5.jpg', 0)

# Sobel算子
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.hypot(sobelx, sobely)
sobel = np.uint8(sobel / np.max(sobel) * 255)
# Laplacian算子
                        
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))


scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharr = np.hypot(scharrx, scharry)
scharr = np.uint8(scharr / np.max(scharr) * 255)


# 显示结果
plt.subplot(1, 3, 1), plt.imshow(sobel, cmap='gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(scharr, cmap='gray')
plt.title('scharr'), plt.xticks([]), plt.yticks([])
plt.show()