#Import libraries
import cv2
import numpy as np
#Read the image
image=cv2.imread("Kielce.jpg")
#Add rectangle on the image
drawingRectangle=cv2.rectangle(image,(400,400),(800,800),(255,0,0),3)
#Add rectangle on the numpy matrix
drawingRectangleNumpy=np.zeros((400,400,3),dtype='uint8')
cv2.rectangle(drawingRectangleNumpy,(200,200),(250,250),(0,255,255),3)
#Show Result
cv2.imshow("Drawing Rectangle",drawingRectangle)
cv2.imshow("Numpy Rectangle",drawingRectangleNumpy)

cv2.waitKey(0)
cv2.destroyAllWindows()
