import cv2
image=cv2.imread('C:/Users/mohit/Downloads/tiger.jpg')
cv2.imshow('original',image)
cv2.waitKey(500)
blurimage=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('blurimage',blurimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
