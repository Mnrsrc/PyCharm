import cv2
import numpy as np
image=cv2.imread('sunflower.jpg')
cv2.imshow("Sun Flower",image)

print("Shape of İmage:" + str(image.shape))
#Show the Pixel Value
print("Pixel value of (80,80) coordinat points:",str(image[20,20]))
image[20,20]=[0,255,255]
print("Pixel value of (80,80) coordinat points:",str(image[20,20]))
#Show the Region Value
region=image[0:210,45:300]
cv2.imshow("Region",region)
#Add region to original image
#IT DOES NOT WORK!!!
#image[550:760,205:460]=region
cv2.rectangle(image,(45,0),(300,210),(0,255,255),2)
#Fill in the fields with white
cv2.imshow("Sun Flower2",image)
cv2.waitKey(0)
cv2.destroyAllWindows()