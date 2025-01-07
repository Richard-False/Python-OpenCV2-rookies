import cv2
import numpy as np

image = cv2.imread(r'picture1.jpg')
rows, cols, ch = image.shape

# 原图中的三个点以及它们在输出图像中的位置
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
# 生成仿射变换矩阵
M = cv2.getAffineTransform(pts1, pts2)
# 应用仿射变换
warped_image = cv2.warpAffine(image, M, (cols, rows))
# 显示结果
cv2.namedWindow('Image', cv2.WINDOW_NORMAL) 
cv2.imshow('Image', image)
cv2.namedWindow('warped_image', cv2.WINDOW_NORMAL) 
cv2.imshow('warped_image', warped_image)
cv2.resizeWindow('Image', 400,300)
cv2.resizeWindow('warped_image', 400,300)
cv2.waitKey(0)
cv2.destroyAllWindows()
