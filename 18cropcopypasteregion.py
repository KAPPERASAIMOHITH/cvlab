import cv2

# Read the source image
source_image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg')

# Display the source image
cv2.imshow('Source Image', source_image)
cv2.waitKey(0)

# Define the region of interest (ROI) coordinates (x, y, width, height)
x, y, width, height = 100, 100, 200, 200
roi = source_image[y:y+height, x:x+width]

# Display the ROI
cv2.imshow('ROI', roi)
cv2.waitKey(0)

# Paste the ROI into a new location in the source image
new_x, new_y = 300, 300
source_image[new_y:new_y+height, new_x:new_x+width] = roi

# Display the modified image with the ROI pasted
cv2.imshow('Modified Image', source_image)
cv2.waitKey(0)

# Save the modified image
cv2.imwrite('modified_image.jpg', source_image)

# Close all OpenCV windows
cv2.destroyAllWindows()
