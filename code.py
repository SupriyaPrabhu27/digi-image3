import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('parrot.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.show()

plt.hist(img.ravel(), 256, range=[0,256])
plt.title('Original Image Histogram')
plt.show()

img_eq = cv2.equalizeHist(img)

plt.hist(img_eq.ravel(), 256, range=[0,256])
plt.title('Equalized Histogram')
plt.show()

plt.imshow(img_eq, cmap='gray')
plt.title('Equalized Image')
plt.show()

img = cv2.imread('parrot.jpg', cv2.IMREAD_COLOR)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])

img_eq = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

plt.subplot(121)
plt.imshow(img[:, :, ::-1])
plt.title('Original Color Image')

plt.subplot(122)
plt.imshow(img_eq[:, :, ::-1])
plt.title('Equalized Image')

plt.show()

plt.figure(figsize=[12,10])

plt.subplot(221)
plt.imshow(img[:, :, ::-1])
plt.title('Original Color Image')

plt.subplot(222)
plt.imshow(img_eq[:, :, ::-1])
plt.title('Equalized Image')

plt.subplot(223)
plt.hist(img.ravel(), 256, range=[0,256])
plt.title('Original Histogram')

plt.subplot(224)
plt.hist(img_eq.ravel(), 256, range=[0,256])
plt.title('Histogram Equalized')

plt.show()
