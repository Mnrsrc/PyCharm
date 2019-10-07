import cv2
image=cv2.imread('autumn.jpg')
imageGray=cv2.imread('autumn.jpg',0)
cv2.imshow('Autumn Picture',image)
cv2.imshow("Gray Picture",imageGray)
cv2.imwrite('grayAutmunPicture.jpg',imageGray)
cv2.imwrite("autumnGrayPng.png",imageGray)
cv2.waitKey(0)
cv2.destroyAllWindows()