import cv2

# Load the cascade classifier
watch_cascade = cv2.CascadeClassifier("C:/Users/mohit/Downloads/watch_cascade.xml")  # Replace 'watch_cascade.xml' with the path to your trained cascade classifier file

# Read the image
image = cv2.imread("C:/Users/mohit/Downloads/watchimage.jpg")  # Replace 'image.jpg' with the path to your input image

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect watches in the image
watches = watch_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected watches
for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the result
cv2.imshow('Detected Watches', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
