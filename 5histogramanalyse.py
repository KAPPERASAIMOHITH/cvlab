import cv2
from matplotlib import pyplot as plt
image = cv2.imread('C:/Users/mohit/Downloads/tiger.jpg')
blue, green, red = cv2.split(image)
hist_blue = cv2.calcHist([blue], [0], None, [256], [0, 256])
hist_green = cv2.calcHist([green], [0], None, [256], [0, 256])
hist_red = cv2.calcHist([red], [0], None, [256], [0, 256])
plt.figure(figsize=(10, 6))
plt.plot(hist_red, color='red')
plt.plot(hist_green, color='green')
plt.plot(hist_blue, color='blue')
    
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
plt.legend(['Red', 'Green', 'Blue'])
plt.xlim([0, 256])
plt.show()
  

