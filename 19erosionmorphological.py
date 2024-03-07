import cv2
import numpy as np

# Read the image
image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg', 0)  # Read the image in grayscale

# Define the kernel for erosion
kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel with all ones

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
