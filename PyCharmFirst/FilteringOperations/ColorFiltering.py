#import libraries
import  cv2
import  numpy as np
from  matplotlib import pyplot as plt

#Open webcam
camera=cv2.VideoCapture(0)
#It is up to 1 that is True
while(1):
    ret,image=camera.read()
    #Convert to hsv color range because of it can be convertable more then easy from bgr
    hsvImage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    # Filter to red range
    upRed=np.array([179,255,255])
    lowRed=np.array([161,155,84])
#Filter to blue
    lowBlue=np.array([94,80,2])
    upBlue=np.array([126,255,255])
    #Filter to green
    lowGreen=np.array([25,52,72])
    upGreen=np.array([102,255,255])
#Masking
    maskedImageR=cv2.inRange(hsvImage,lowRed,upRed)
    maskedImageB=cv2.inRange(hsvImage,lowBlue,upBlue)
    maskedImageG=cv2.inRange(hsvImage,lowGreen,upGreen)
    #Comparision bitwise
    lastImageR=cv2.bitwise_and(image,image,mask=maskedImageR)
    lastImageB=cv2.bitwise_and(image,image,mask=maskedImageB)
    lastImageG=cv2.bitwise_and(image,image,mask=maskedImageG)
    cv2.imshow("Normal Image", image)
    cv2.imshow("Green Mask",maskedImageG)
    cv2.imshow("Latest Image",lastImageG)
    #For BLUE Mask
    cv2.imshow("Blue Mask",maskedImageB)
    cv2.imshow("Latest Image",lastImageB)
    #Save the image
    cv2.imwrite("MaskBlue.jpg",lastImageB)
    if cv2.waitKey(25) & 0XFF == ord('q'):
        break
#For GREEN Mask
"""cv2.imshow("Green Mask",maskedImageG)
cv2.imshow("Latest Image",lastImageG)"""

#For RED Mask
"""cv2.imshow("Red Mask",maskedImageR)
cv2.imshow("Latest image",lastImageR)"""



# showing to all of image.If you want to see all of masked picture, run the following code

"""plt.subplot(331),plt.imshow(image,'pink'),plt.title("Normal")
        plt.subplot(332), plt.imshow(image,'pink'), plt.title("Normal")
        plt.subplot(333), plt.imshow(image,'pink'),plt.title("Normal")

        plt.subplot(334),plt.imshow(maskedImageR,'pink'), plt.title("Red Mask")
        plt.subplot(335),plt.imshow(maskedImageG,'pink'), plt.title("Green Mask")
        plt.subplot(336),plt.imshow(maskedImageB,'pink'), plt.title("Blue Mask")

        plt.subplot(337),plt.imshow(lastImageR,'pink'), plt.title("RED")
        plt.subplot(338),plt.imshow(lastImageG,"pink"), plt.title("GREEN")
        plt.subplot(339),plt.imshow(lastImageB,"pink"),plt.title("BLUE")

        plt.show()"""




camera.release()
cv2.destroyAllWindows()
#Close

cv2.destroyAllWindows()