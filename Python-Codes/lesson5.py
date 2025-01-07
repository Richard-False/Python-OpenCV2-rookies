import cv2
import numpy as np

# create an image 'zeros' meaning all initial values are 0==black
#the tuple is a symbol of RGB image
#(height,width,3) np.uint8 is a datatype for pixels
img = np.zeros((512, 512, 3), np.uint8)

###Create certain shapes
#LINE: image_name,starting point, ending point, color in RGB, thickness of the line
cv2.line(img, (0, 0), (511, 511), (255, 255, 255), 5)
#RECTANGLE: lefttop point, rightlow point,color,thickness
cv2.rectangle(img, (384, 0), (510, 128), (255, 0, 0), 3)
#CIRCLE: center points, radius___(-1 means the thickness is whole part inside)
cv2.circle(img, (256, 256), 100, (0, 0, 255), -1)
#ELLIPSE: centerpoint, length of axises(longer,shorter),
#angle, startAngle, endAngle,-1as before
#angle meaning the angle between the x-axis and the long axis of the ellipse
#the two angles behind start and end
cv2.ellipse(img, (256, 256), (100, 50), 0, 50, 360, 255, -1)
#POLYGON:to create a polygon, we need each points' x and y value_in int form
#and that ought to be set in a list(pts)
#np.reshape()我暂时没看懂。。。
#name.reshape(image,[list],whether the polygon is a shut one,(RGB),thickness of the pixel)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 0), 3)
#TEXT:cv2.putText(img, 内容, 文字起始位置, 文字格式, 文字大小, color, thickness = 1, lineType = cv2.LINE_AA)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

###Edit figures(shapes)
px = img[100, 100]  #acquire pixel
img[100, 100] = [255, 255, 255]#change pixel
print(img.shape)  # return a tuple representing the shape of the figure
print(img.size)   # return the number of the pixels in a shape
print(img.dtype)  # return the datatype of a figure
# cut the ROI(certain areaof a figure)and copy to sth else
face = img[100:200, 115:188]
img[0:100, 0:73] = face

cv2.imshow('Line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
