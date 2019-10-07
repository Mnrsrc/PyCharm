import cv2
import numpy as np

image=cv2.imread('october5.jpg')

#USAGE 1
b,g,r=cv2.split(image)
image=cv2.merge((b,g,r))
print("Blue Points"  + str(image[:,:,0]))
print("Green Points: " + str(image[:,:,1]))
print("Red Points: " + str(image[:,:,2]))
bluePixels=image[:,:,0]
greenPixels=image[:,:,1]
redPixels=image[:,:,2]
#image[:,:,1]=200
cv2.imwrite("GreenOctober.jpg",image)
#cv2.imshow("Blue Pixels",bluePixels)
cv2.imshow("İmage",image)
#USAGE 2
#blue=image[:,:,2]
#blue=0

cv2.waitKey(0)
cv2.destroyAllWindows()
