import cv2

image = cv2.imread(r'map.jpg')
rows, cols = image.shape[:2]

# 旋转中心点为图像中心，旋转角度为90度，不改变图像尺寸
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
rotated_image = cv2.warpAffine(image, M, (cols, rows))
#cv2.getRotationMatrix2D(center, angle, scale)
#when processing normal M for cv2.warpAffine
#We use like this:
#M = np.float32( [ [a,b,c],
#                           [d,e,f] ] )

cv2.namedWindow('Image', cv2.WINDOW_NORMAL) 
cv2.imshow('Image', rotated_image)
cv2.resizeWindow('Image', 800, 600)
cv2.waitKey(0)
cv2.destroyAllWindows()