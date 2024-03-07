import cv2
image=cv2.imread('C:/Users/mohit/Downloads/tiger.jpg')
grayimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
equalisedimage=cv2.equalizeHist(grayimage)
cv2.imshow('original',image)
cv2.imshow('grayimage',grayimage)
cv2.imshow('equalisedimage',equalisedimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
