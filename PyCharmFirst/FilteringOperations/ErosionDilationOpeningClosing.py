#import libraries
import  cv2
import  numpy as np
#Take an image
image = cv2.imread("51.jpg")
#masking
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lowSkinColor=np.array([0,58,30])
upSkinColor=np.array([33,255,255])
hsvMaskSkin=cv2.inRange(hsv,lowSkinColor,upSkinColor)
#Comparision Bitwise
BitwiseHsvSkin=cv2.bitwise_and(image,image,mask=hsvMaskSkin)
#Erosion Processing
"""kernel=np.ones((5,5),np.uint8)
erosion=cv2.morphologyEx(image,kernel,iterations=1)"""
#Dilation Processing
#Opening
#Closing
#Show result
cv2.imshow("Original",image)
cv2.imshow("hsvMaskSkin",hsvMaskSkin)
cv2.imshow("BitwiseHsvSkin",BitwiseHsvSkin)
#Close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()