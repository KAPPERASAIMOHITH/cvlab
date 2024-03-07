import cv2

image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg')

flipped_image = cv2.flip(image, 1)

rotated_image = cv2.transpose(flipped_image)

cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

