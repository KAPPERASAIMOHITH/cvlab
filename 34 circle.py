import cv2
import numpy as np

def create_circle_image(size):
    image = np.ones((size, size, 3), dtype=np.uint8) * 255
    center = (size // 2, size // 2)
    radius = min(size // 4, size // 3)
    cv2.circle(image, center, radius, (0, 0, 0), thickness=2)
    cv2.imshow('Circle Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
size = int(input("Enter the size of the image: "))
create_circle_image(size)
