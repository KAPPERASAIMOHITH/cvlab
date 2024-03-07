import cv2
import numpy as np

# Load the input image
image_path = "C:/Users/mohit/Downloads/faces1.jpg"  # Replace 'example_image.jpg' with the path to your image file
image = cv2.imread(image_path)

# Convert BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the color to be extracted
lower_color = np.array([0, 50, 50], dtype=np.uint8)  # Lower bound of the color (in HSV format)
upper_color = np.array([10, 255, 255], dtype=np.uint8)  # Upper bound of the color (in HSV format)

# Threshold the HSV image to get only the specified color range
mask = cv2.inRange(hsv_image, lower_color, upper_color)

# Bitwise-AND mask and original image
foreground = cv2.bitwise_and(image, image, mask=mask)

# Display the original and foreground-subtracted images
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Foreground Subtracted Image', foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()
