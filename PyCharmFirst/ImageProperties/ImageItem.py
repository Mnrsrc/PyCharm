import cv2
import numpy as np
from docutils.nodes import image
from sympy import im

image=cv2.imread('nature.jpg')
cv2.imshow("Nature",image)

print("Blue pixel sizes of image:" + str(image.item(100,100,0)))
print("Green pixel sizes of image:" + str(image.item(150,150,1)))
print("Red pixel sizes of image:" + str(image.item(160,160,2)))
print("Image Shape" + str(image.shape))
#??????
#image2=image.itemset((100,100,2),255)
#cv2.imshow("Red Nature",image2)
image3=cv2.imread('nature.jpg',0)
cv2.imwrite("GrayNature.jpg",image3)
print("Gray Nature Shape:" + str(image3.shape))
print("Pixel size of original picture: " + str(image.size))
print("Pixel Size of gray picture:" + str(image3.size))
print("Data type of original image:" + str(image.dtype))



cv2.waitKey(0)
cv2.destroyAllWindows()