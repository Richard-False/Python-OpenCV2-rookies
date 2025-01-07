import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread(r'picture6.jpg',cv2.IMREAD_GRAYSCALE)
image_mean = cv2.blur(image,(5, 5))#均值滤波（image,(a,b)size of the kernel）
image_Gaussian = cv2.GaussianBlur(image,(5,5),100)#高斯滤波(image,(a,b)kernel,c标准差)
image_median = cv2.medianBlur(image,5)#中值滤波(image,kernel)

#extra statements：
#均值滤波和高斯滤波是线性滤波，采用均值或加权求和来进行计算，可二维定义核
#中值滤波是对于周围的像素值排序取中值，是非线性的所以采用正方形核
plt.figure(figsize=(8, 4))#size of the figure created(width, height)

plt.subplot(1, 3, 1)#generate many figures at the same time
plt.title('mean')#one row, three colomn, the first one
plt.imshow(image_mean,cmap='grey')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Gaussian')
plt.imshow(image_Gaussian,cmap='grey')

plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('median')
plt.imshow(image_median,cmap='grey')
plt.axis('off')

plt.tight_layout()#automatically set the space \
#between the pictures to make it more beautiful
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()