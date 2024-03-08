import cv2
import numpy as np
def add_text_to_image(text, image_size):
    image = 255 * np.ones((image_size, image_size, 3), dtype=np.uint8)
    cv2.putText(image, text, (image_size // 4, image_size // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('Image with Text', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

text = input("Enter the text to appear on the image: ")
image_size = int(input("Enter the size of the image: "))
add_text_to_image(text, image_size)
