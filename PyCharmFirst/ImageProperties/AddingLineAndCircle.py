#Add to libraries
import cv2
import  numpy as np
#Read the image or make a matrix
image=cv2.imread('Breakfast.jpg')
resolution=200,200
#Resize the image
scaleWidth=resolution[0]/image.shape[1]
scaleHeight=resolution[1]/image.shape[0]
scale=min(scaleHeight,scaleWidth)
windowHeight=int(scale*image.shape[0])
windowWidth=int(scale*image.shape[1])
cv2.resizeWindow("Resized Window",windowWidth,windowHeight)
#Draw to line
cv2.line(image,(0,0),(250,130),(255,255,0),3)
cv2.line(image,(220,100),(250,130),(255,255,0),3)
cv2.line(image,(220,140),(250,130),(255,255,0),3)

#Draw to circle
cv2.circle(image,(370,260),120,(255,255,0),3)
#Show results
cv2.imshow('Breakfast',image)
#Finish
cv2.waitKey(0)
cv2.destroyAllWindows()