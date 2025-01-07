import cv2
import matplotlib.pyplot as plt
#use grey scale to read a picture
image = cv2.imread(r'picture1.jpg', cv2.IMREAD_GRAYSCALE)

# mean
adaptive_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)
# gaussian
adaptive_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
#cv2.adaptiveThreshold(image,value of the pixel when processed,method,
# #if||if not,the final slight change)
#increase the '2'constant C to reduce the noises
# SHOE THE CONTRASTING PICTURES
plt.figure(figsize=(8, 4))#size of the figure created(width, height)

plt.subplot(1, 2, 1)#generate many figures at the same time
plt.title('Adaptive Mean')#one row, three colomn, the first one
plt.imshow(adaptive_mean, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Adaptive Gaussian')
plt.imshow(adaptive_gaussian, cmap='gray')
plt.axis('off')

plt.tight_layout()#automatically set the space \
#between the pictures to make it more beautiful
plt.show()