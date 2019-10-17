import cv2
import numpy as np
#Laiding İmages
image1=cv2.imread("mirror.jpg")
image2=cv2.imread("angelinaJolie2.jpg")
#Row, column and channel size
row,column,channel=image2.shape
print("Row:" + str(row))
print("Column:" + str(column))
print("Channel:" + str(channel))
print("Shape of İmage1:" + str(image1.shape))
#ROİ=REGİON OF IMAGE
roi=image1[194:810,400:734]
cv2.imshow("Roi",roi)
#Filtering to image2
image2Gray=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray of image2:",image2Gray)
#Determining to Threshold
ret,mask=cv2.threshold(image2Gray,10,255,cv2.THRESH_BINARY)
cv2.imshow("ret",mask)
#Bitwise to mask of image2/ Inverted to mask
maskInverted=cv2.bitwise_not(mask)
cv2.imshow("Inverted Mask",maskInverted )
#image1Background=cv2.bitwise_and(roi,roi,mask=maskInverted)
#cv2.imshow("Background of image1",image1Background)







































cv2.waitKey(0)
cv2.destroyAllWindows()