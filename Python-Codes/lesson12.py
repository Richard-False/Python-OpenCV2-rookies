import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'picture3.jpg', cv2.IMREAD_GRAYSCALE)  # 以灰度模式读取图像
edges = cv2.Canny(image, 150, 200)  # 应用Canny边缘检测

plt.figure(figsize=(16,8))
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(image,cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title('Edges')
plt.imshow(edges,cmap='gray')
plt.axis('off')

plt.tight_layout()#automatically set the space \
#between the pictures to make it more beautiful
plt.show()