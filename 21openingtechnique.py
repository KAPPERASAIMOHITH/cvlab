import cv2
import numpy as np

# Read the image
image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg', 0)  # Read the image in grayscale

# Define the kernel for opening
kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel with all ones

# Apply opening (erosion followed by dilation)
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Display the original and opened images
cv2.imshow('Original Image', image)
cv2.imshow('Opened Image', opened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
