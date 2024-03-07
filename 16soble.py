import cv2

image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg', cv2.IMREAD_GRAYSCALE)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.sqrt(cv2.addWeighted(cv2.pow(sobel_x, 2.0), 1.0, cv2.pow(sobel_y, 2.0), 1.0, 0.0))
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Filtered Image', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
