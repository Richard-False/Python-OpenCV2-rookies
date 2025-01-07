import cv2
import numpy as np
image = cv2.imread(r'C:\Users\pc\Desktop\picture1.jpg')
#use cvt to change thepicture to its grey form
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#in this p[art we set the range of "blue" using 3 symbols of the HSV
#Hue色相: The type of color, like red, green, or blue, represented by a degree on the color wheel (0° to 360°).
#Saturation饱和度: The intensity of the color, from gray (0%) to full color (100%).
#Value明度: The brightness of the color, from black (0%) to full brightness (100%).

#see the arrays like a matrix,(110,130)__Hue  (50,255)__Saturation  (50,255)__Value
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
#use line 15 to select all the "blue" pixels inthe image
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
#do nthe bitwise operation of AND between the mask(selected part) and the whole image to separate them off
blue_object = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Original image', image)
cv2.imshow('Blue object', blue_object)
cv2.waitKey(0)
cv2.destroyAllWindows()
