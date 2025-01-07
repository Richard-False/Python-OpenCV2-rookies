import cv2
import numpy as np
foreground = cv2.imread(r'map.jpg')
background = cv2.imread(r'picture1.jpg')
mask = cv2.imread(r'map.jpg', 0)
#前景；背景，mask掩码 as mask approaches to 0 the part of the background appears
#more accurate, as it approaches to 255 the frontground appears more clearly
reference_size = foreground.shape[:2]
# .shape returns a tuple(height,width,channels(if colors,==3, grey ==1))
# and in this line it choose the size not the channels
background = cv2.resize(background, (reference_size[1], reference_size[0]))
mask = cv2.resize(mask, (reference_size[1], reference_size[0]))
#cv2.resize(image, dsize(width,height), fx=0, fy=0,
#interpolation插值方式（怎么样resize）=cv2.INTER_LINEAR)
#cv2.INTER_NEAREST快速但是品质不佳
#cv2.INTER_LINEAR线性插值，适用于缩放
#cv2.INTER_AREA区域插值，适用于缩小
#cv2.INTER_CUBIC三次样条插值，适用于放大
#cv2.INTER_LANCZOS4超级精细化
print("Foreground shape:", foreground.shape)
print("Background shape:", background.shape)
print("Mask shape:", mask.shape)
#debug
if foreground is None or background is None or mask is None:
    print("Error: One or more images could not be loaded. Check file paths.")
    exit()
if foreground.shape[:2] != background.shape[:2] or foreground.shape[:2] != mask.shape[:2]:
    print("Error: Images or mask dimensions do not match.")
    exit()

foreground = cv2.bitwise_and(foreground, foreground, mask=mask)
#mask!=0 ->save the result as and
#to extract the frontground
background = cv2.bitwise_and(background, background, mask=cv2.bitwise_not(mask))
result = cv2.add(foreground, background)

cv2.namedWindow('Image', cv2.WINDOW_NORMAL) 
cv2.imshow('Image', result)
cv2.resizeWindow('Image', 800, 600)
cv2.waitKey(0)
cv2.destroyAllWindows()
