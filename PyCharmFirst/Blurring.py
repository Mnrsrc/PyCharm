#import Libraries
import cv2
import  numpy as np
#Input an image
image=cv2.imread('park.jpg')
#Bluring the image by some blurring methods:
#1-Filter2D, (150,140) matrix, 150*140=21000
kernel=np.ones((150,140),np.float32)/21000
smoothedImage=cv2.filter2D(image,-1,kernel)
#2-gaussianBlur,matrix (120,130)
gaussianBlur=cv2.GaussianBlur(image,(15,15),0)
#3-Median Blur
medianBlurred=cv2.medianBlur(image,15)
#4-Bilateral Blur
bilateralImage=cv2.bilateralFilter(image,15,180,180)
#Show the results
cv2.imshow('Original Image',image)
cv2.imshow('Smoothed Image',smoothedImage)
cv2.imshow('Blurred Image',gaussianBlur)
cv2.imshow('Median Blur',medianBlurred)
cv2.imshow('Bilateral',bilateralImage)
#Save the blurring images
cv2.imwrite('SmoothedImage.jpg',smoothedImage)
cv2.imwrite('Gaussian Blurred Image.jpg', gaussianBlur)
cv2.imwrite('MedianBlur.jpg', medianBlurred)
cv2.imwrite('Bilateral.JPG',bilateralImage)
#close the window.
cv2.waitKey()
cv2.destroyAllWindows()

