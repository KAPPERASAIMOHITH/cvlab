import cv2
import numpy as np
image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray_image, 2, 3, 0.04)
threshold = 0.01 * dst.max()
corner_image = np.copy(image)
corner_image[dst > threshold] = [0, 0, 255] 
cv2.imshow('Original Image with Corners', corner_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
