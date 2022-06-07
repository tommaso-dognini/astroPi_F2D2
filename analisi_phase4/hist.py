# https://www.geeksforgeeks.org/opencv-python-program-analyze-image-using-histogram/ 

# importing required libraries of opencv
from cProfile import label
import cv2
# importing library for plotting
from matplotlib import pyplot as plt


# reads an input image as colored
img = cv2.imread('img/ndvi/ndvi58.jpg')


# BLUE
# find frequency of pixels in range 0-255
hist_b = cv2.calcHist([img],[0],None,[256],[0,256])
# show the plotting graph of an image
plt.plot(hist_b, color="blue",label='Blue channel')

#GREEN
# find frequency of pixels in range 0-255
hist_g = cv2.calcHist([img],[1],None,[256],[0,256])
# show the plotting graph of an image
plt.plot(hist_g, color="green",label='Green channel')

#RED
# find frequency of pixels in range 0-255
hist_r = cv2.calcHist([img],[2],None,[256],[0,256])
# show the plotting graph of an image
plt.plot(hist_r, color="red",label='Red channel')
plt.ylim(0,100000)

plt.title('RGB channels pixel intensity')
plt.xlabel('Color (0,255)')
plt.ylabel('Frequency')
plt.legend()
plt.show()


