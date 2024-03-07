import cv2

video_path = "C:/Users/mohit/Downloads/pexels_videos_1456996 (1080p).mp4"
video = cv2.VideoCapture(video_path)
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

current_frame = total_frames - 1

while current_frame >= 0:
    video.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    ret, frame = video.read()
    if ret:
        cv2.imshow('Video in Reverse', frame)
        cv2.waitKey(30)
    else:
        break
    current_frame -= 1

video.release()
cv2.destroyAllWindows()
