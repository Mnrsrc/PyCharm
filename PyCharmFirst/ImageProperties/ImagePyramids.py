#There are 2 types image pyramids.
#In here, it is used the Gauss Pyramid method
#import library
import cv2

#Read the image
image=cv2.imread("Kielce.jpg")
#Resolution upgrading
upperImage=cv2.pyrUp(image)
#Reduce the resolution
lowerImage=cv2.pyrDown(image)
#Show the results
cv2.imshow("Normal Image",image)
cv2.imshow("Upgrade Image",upperImage)
cv2.imshow("Reduce Image", lowerImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

