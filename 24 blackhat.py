import cv2
import numpy as np
image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg', 0) 
kernel = np.ones((5, 5), np.uint8)  
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
black_hat = cv2.subtract(closing, image)
cv2.imshow('Original Image', image)
cv2.imshow('Black Hat Image', black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
