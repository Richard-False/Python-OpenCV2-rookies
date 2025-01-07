import cv2
import numpy as np

image = cv2.imread(r'picture1.jpg')
rows, cols, ch = image.shape

# 旋转后的仿射变换
M_rot = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
rotated_image = cv2.warpAffine(image, M_rot, (cols, rows))

# 仿射变换的三点
pts1 = np.float32([[100, 100], [200, 100], [100, 200]])
pts2 = np.float32([[80, 150], [200, 130], [120, 220]])

M_affine = cv2.getAffineTransform(pts1, pts2)
warped_image = cv2.warpAffine(rotated_image, M_affine, (cols, rows))

# 显示结果
cv2.namedWindow('Image', cv2.WINDOW_NORMAL) 
cv2.imshow('Image', image)
cv2.namedWindow('warped_image', cv2.WINDOW_NORMAL) 
cv2.imshow('warped_image', warped_image)
cv2.resizeWindow('Image', 400,300)
cv2.resizeWindow('warped_image', 400,300)
cv2.waitKey(0)
cv2.destroyAllWindows()
