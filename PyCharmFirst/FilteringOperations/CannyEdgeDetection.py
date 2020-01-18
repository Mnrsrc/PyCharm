#import libraries
import cv2
from matplotlib import pyplot as plt
#Take an image
image=cv2.imread('building.jpg')
#Detect Edge some methods
cannyDetect=cv2.Canny(image,50,50)
cannyDetect2=cv2.Canny(image,200,150)
laplacianDetect=cv2.Laplacian(image,cv2.CV_64F)
#When I set ksize=4, it did not work
sobelX=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
sobelY=cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
#Show results


cv2.imshow('Image',image)
cv2.imshow('Canny Detect', cannyDetect)
cv2.imshow('Canny Detect2',cannyDetect2)
cv2.imshow('Laplacian Detect',laplacianDetect)
cv2.imshow('SobelX',sobelX)
cv2.imshow("SobelY",sobelY)
#Save results
cv2.imwrite("CannyDetection.jpg",cannyDetect)
cv2.imwrite("CannyDetection2.jpg",cannyDetect2)
cv2.imwrite("LaplacianDetection.jpg", laplacianDetect)
cv2.imwrite("SobelX.jpg",sobelX)
cv2.imwrite("SobelY.jpg",sobelY)
"""plt.subplot(321),plt.imshow(image,cmap="gray")
plt.title("Normal"),plt.xticks([]),plt.yticks([])
plt.subplot(322),plt.imshow(cannyDetect,cmap="gray")
plt.title("Canny Detect"),plt.xticks([]),plt.yticks([])
plt.subplot(323),plt.imshow(cannyDetect2,cmap="gray")
plt.title("Canny Detect2"),plt.xticks([]),plt.yticks([])
plt.subplot(324),plt.imshow(laplacianDetect,cmap="gray")
plt.title("Laplacian"),plt.xticks([]),plt.yticks([])
plt.subplot(325),plt.imshow(sobelX,cmap="gray")
plt.title("SobelX"),plt.xticks([]),plt.yticks([])
plt.subplot(326),plt.imshow(sobelY,cmap="gray")
plt.title("SobelY"),plt.xticks([]),plt.yticks([])
plt.show()"""
#Close windows
cv2.waitKey()
cv2.destroyAllWindows()