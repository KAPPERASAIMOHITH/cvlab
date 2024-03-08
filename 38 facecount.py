import cv2
image_path = "C:/Users/mohit/Downloads/faces1.jpg"  # Replace 'example_image.jpg' with the path to your image file
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
num_faces = len(faces)
print("Number of faces detected:", num_faces)
