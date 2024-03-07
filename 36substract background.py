import cv2
import numpy as np

# Load the input image
image_path = 'C:/Users/mohit/Downloads/faces1.jpg'  # Replace 'example_image.jpg' with the path to your image file
image = cv2.imread(image_path)

# Convert BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the color to be extracted
lower_color = np.array([0, 50, 50], dtype=np.uint8)  # Lower bound of the color (in HSV format)
upper_color = np.array([10, 255, 255], dtype=np.uint8)  # Upper bound of the color (in HSV format)

# Threshold the HSV image to get only the specified color range
mask = cv2.inRange(hsv_image, lower_color, upper_color)

# Invert the mask to get the background
background = cv2.bitwise_not(mask)

# Bitwise-AND mask and original image to get the foreground
foreground = cv2.bitwise_and(image, image, mask=mask)

# Bitwise-AND inverted mask and original image to get the background
background = cv2.bitwise_and(image, image, mask=background)

# Subtract background from the original image to get the result
result = cv2.subtract(image, background)

# Display the original image, foreground, background, and result
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Foreground', foreground)
cv2.imshow('Background', background)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
