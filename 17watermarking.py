import cv2

original_image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg')
watermark_image = cv2.imread("C:/Users/mohit/Downloads/watermarked.jpg", cv2.IMREAD_UNCHANGED)
watermark_height, watermark_width, _ = watermark_image.shape
scale_factor = 0.2  
resized_watermark = cv2.resize(watermark_image, (int(watermark_width * scale_factor), int(watermark_height * scale_factor)))
position_x = 20
position_y = 20
roi = original_image[position_y:position_y+resized_watermark.shape[0], position_x:position_x+resized_watermark.shape[1]]
alpha = 0.5  
watermarked_roi = cv2.addWeighted(roi, 1 - alpha, resized_watermark[:, :, :3], alpha, 0)
original_image[position_y:position_y+resized_watermark.shape[0], position_x:position_x+resized_watermark.shape[1]] = watermarked_roi
cv2.imshow('Watermarked Image', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
