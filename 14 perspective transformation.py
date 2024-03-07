import cv2
import numpy as np
image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg')

src_points = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
dst_points = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(src_points, dst_points)
transformed_image = cv2.warpPerspective(image, M, (300, 300))
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
