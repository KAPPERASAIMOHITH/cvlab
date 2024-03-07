import cv2
image=cv2.imread('C:/Users/mohit/Downloads/tiger.jpg')
cv2.imshow('original',image)
cv2.waitKey(0)
grayimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cannyedgeimage=cv2.Canny(grayimage,100,200)
cv2.imshow('grayimage',cannyedgeimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
