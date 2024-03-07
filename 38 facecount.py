import cv2

# Load the input image
image_path = "C:/Users/mohit/Downloads/faces1.jpg"  # Replace 'example_image.jpg' with the path to your image file
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Count the number of faces detected
num_faces = len(faces)

print("Number of faces detected:", num_faces)
