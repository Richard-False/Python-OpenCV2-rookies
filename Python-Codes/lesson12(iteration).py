import cv2
import keyboard
import matplotlib.pyplot as plt
image = cv2.imread(r'picture8.jpg', cv2.IMREAD_GRAYSCALE)
#initialize the high and low threshold
high_threshold = 100
low_threshold = 50

def new_func(image, high_threshold, low_threshold):
    edges = cv2.Canny(image, low_threshold, high_threshold)
    return edges

while True:
    edges = new_func(image, high_threshold, low_threshold)

    plt.figure(figsize=(16,8))
    plt.subplot(1,2,1)
    plt.title('Original Image')
    plt.imshow(image,cmap='gray')
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.title('Edges')
    plt.imshow(edges,cmap='gray')
    plt.axis('off')

    plt.tight_layout()#automatically set the space \
    #between the pictures to make it more beautiful
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    response = input("Are U satisfied with the result？(y/n)")
    event = keyboard.read_event()
    if event.name == 'enter':
        break
    else:

        if response == 'y':
            break
        adjust = input("input to adjust the threshold (h:up the high-threshold, l:lower the high-threshold, H:up the low-threshold, L:lower the low-threshold")
        if adjust == 'h':
            high_threshold += 10
        elif adjust == 'l':
            high_threshold -= 10
        elif adjust == 'H':
            low_threshold += 10
        elif adjust == 'L':
            low_threshold -= 10
