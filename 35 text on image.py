import cv2
import numpy as np

def add_text_to_image(text, image_size):
    image = np.ones((image_size, image_size, 3), dtype=np.uint8) * 255
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 1, 2)[0]
    text_x = (image_size - text_size[0]) // 2
    text_y = (image_size + text_size[1]) // 2
    cv2.putText(image, text, (text_x, text_y), font, 1, (0, 0, 0), 2)
    cv2.imshow('Image with Text', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
text = input("Enter the text to appear on the image: ")
image_size = int(input("Enter the size of the image: "))
add_text_to_image(text, image_size)
