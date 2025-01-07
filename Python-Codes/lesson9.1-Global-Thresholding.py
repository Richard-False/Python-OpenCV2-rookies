import cv2
#use grey scale to read a picture
image = cv2.imread(r'picture1.jpg', cv2.IMREAD_GRAYSCALE)
image0 = cv2.imread(r'picture1.jpg', cv2.IMREAD_COLOR)
# Trial 1 :使用全局阈值127，将图像二值化
retval, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
#127是选定的全局阈值。如果某个像素的灰度值大于或等于127
#，该像素点的值将设置为255（白色），否则设置为0（黑色）

cv2.namedWindow('Original Image0', cv2.WINDOW_NORMAL)
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Adaptive Thresholding', cv2.WINDOW_NORMAL) 
cv2.imshow('Original Image', image)
cv2.imshow('Original Image0', image0)
cv2.imshow('Adaptive Thresholding', thresh)
cv2.resizeWindow('Original Image', 400,300)
cv2.resizeWindow('Adaptive Thresholding', 400,300)
cv2.resizeWindow('Original Image0', 400,300)
cv2.waitKey(0)
cv2.destroyAllWindows()
