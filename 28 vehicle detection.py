import cv2
vehicle_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')
input_video = cv2.VideoCapture("C:/Users/mohit/Downloads/carvideo.mp4")  
frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(input_video.get(cv2.CAP_PROP_FPS))
output_video = cv2.VideoWriter('output_detected.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
while True:
    ret, frame = input_video.read()
    if not ret:
        break  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    output_video.write(frame)
input_video.release()
output_video.release()
cv2.destroyAllWindows()
