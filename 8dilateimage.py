import cv2
import numpy as np

image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg')
kernel = np.ones((5,5), np.uint8) 
dilated_image = cv2.dilate(image, kernel, iterations=1)
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

