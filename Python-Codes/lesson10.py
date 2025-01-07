import cv2
import matplotlib.pyplot as plt
import numpy as np

image_GREY = cv2.imread(r'picture1.jpg', cv2.IMREAD_GRAYSCALE)
image_COLOR = cv2.imread(r'picture1.jpg', cv2.IMREAD_COLOR)
#直方图cv2.calHist(image,tunnel,mask,xrange,yrange)
#tunnel:在灰度图像中为[0]，如果是彩色图像，可以传入[0], [1] 或 [2] 来分别计算B、G、R通道的直方图
#mask:choose specific area pf the image to operate,255mean not operate,OR NONE
mask = np.zeros(image_GREY.shape[:2], dtype="uint8")
histogram = cv2.calcHist([image_GREY], [0], None, [256], [0, 256])

plt.plot(histogram)
plt.show()