#import libraries
import  numpy as np
import  cv2
#take an image
image=cv2.imread("Margaret_Sullavan_0013.jpg")
#Create kernel matris
kernelMatris=np.ones((5,5),np.uint8)
#Convert to Hsv
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

#Color range of the human's skin
lowSkinColor=np.array([0,58,30])
upSkinColor=np.array([33,255,255])

#Filtering Blue
lowBlue=np.array([150,30,30])
upBlue=np.array([190,255,255])

#Filtering White
lowWhite=np.array([0,0,140])
upWhite=np.array([256,60,256])

#Filtering Yellow
lowYellow=np.array([5,100,100])
upYellow=np.array([40,255,256])

#Masking
maskSkinColor=cv2.inRange(hsv,lowSkinColor,upSkinColor)
maskBlue=cv2.inRange(hsv,lowBlue,upBlue)
maskWhite=cv2.inRange(hsv,lowWhite,upWhite)
maskYellow=cv2.inRange(hsv,lowYellow,upYellow)

#Comparision Bitwise
BitwiseSkin=cv2.bitwise_and(image,image,mask=maskSkinColor)
BitwiseBlue=cv2.bitwise_or(hsv,hsv,mask=maskBlue)
BitwiseWhite=cv2.bitwise_or(image,image,mask=maskWhite)
BitwiseYellow=cv2.bitwise_and(image,image,mask=maskYellow)

#Erosion Filtering
erosion=cv2.erode(maskSkinColor,kernelMatris,iterations=1)
erosionBlue=cv2.erode(maskBlue,kernelMatris,iterations=1)
erosionWhite=cv2.erode(maskWhite,kernelMatris,iterations=1)
erosionYellow=cv2.erode(maskYellow,kernelMatris,iterations=1)

#Dilation Filtering
dilation=cv2.dilate(maskSkinColor,kernelMatris,iterations=5)
dilationBlue=cv2.dilate(maskBlue,kernelMatris,iterations=1)
dilationWhite=cv2.dilate(maskWhite,kernelMatris,iterations=1)
dilationYellow=cv2.dilate(maskYellow,kernelMatris,iterations=1)
#show the results
cv2.imshow("Original",image)
cv2.imshow("HSV",image)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation)
cv2.imshow("Dilation Blue",dilationBlue)
cv2.imshow("Dilation White",dilationWhite)
cv2.imshow("Dilation Yellow",dilationYellow)
#Destroy all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()