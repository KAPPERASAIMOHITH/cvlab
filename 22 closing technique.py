import cv2
import numpy as np

# Read the image
image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg', 0)  # Read the image in grayscale

# Define the kernel for closing
kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel with all ones

# Apply closing (dilation followed by erosion)
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the original and closed images
cv2.imshow('Original Image', image)
cv2.imshow('Closed Image', closed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
