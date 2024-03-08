import cv2
import numpy as np
image_path = 'C:/Users/mohit/Downloads/faces1.jpg' 
image = cv2.imread(image_path)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_color = np.array([0, 50, 50], dtype=np.uint8)  # Lower bound of the color (in HSV format)
upper_color = np.array([10, 255, 255], dtype=np.uint8)  # Upper bound of the color (in HSV format)
mask = cv2.inRange(hsv_image, lower_color, upper_color)
background = cv2.bitwise_not(mask)
foreground = cv2.bitwise_and(image, image, mask=mask)
background = cv2.bitwise_and(image, image, mask=background)
result = cv2.subtract(image, background)
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Foreground', foreground)
cv2.imshow('Background', background)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
