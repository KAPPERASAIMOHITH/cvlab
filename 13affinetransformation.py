import cv2
import numpy as np

image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg')

M = np.float32([[1, 0, 100], [0, 1, 100]])

transformed_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
