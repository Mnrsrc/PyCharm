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
#Create kernel matris
kernel=np.ones((5,5),np.uint8)
#Erosion Processing
erosion=cv2.erode(hsvMaskSkin,kernel,iterations=1)
#Dilation Processing
dilation=cv2.dilate(hsvMaskSkin,kernel,iterations=1)
#Opening
opening=cv2.morphologyEx(hsvMaskSkin,cv2.MORPH_OPEN,kernel)
#Closing
closing=cv2.morphologyEx(hsvMaskSkin,cv2.MORPH_CLOSE,kernel)
#Show result
cv2.imshow("Original",image)
cv2.imshow("hsvMaskSkin",hsvMaskSkin)
cv2.imshow("BitwiseHsvSkin",BitwiseHsvSkin)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation",dilation)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)
#Close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
