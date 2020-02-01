#import libraries
import  cv2
from matplotlib import  pyplot as plt
#Read an image
image=cv2.imread('house.jpg')
#Theshold the image with different thresholding methods. Threshold returns 2 value.
refuse,thresholdBinary=cv2.threshold(image,0,127,cv2.THRESH_BINARY)
refuse2,thresholdBinary2=cv2.threshold(image,0,127,cv2.THRESH_BINARY_INV)
refuse3,thresholdBinary3=cv2.threshold(image,100,200,cv2.THRESH_TRUNC)
refuse4,thresholdBinary4=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
refuse5,thresholdBinary5=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

#Add to a list results and titles
thresholdList=[image,thresholdBinary,thresholdBinary2,thresholdBinary3,thresholdBinary4,thresholdBinary5]
titleList=["Original Image","Binary(0,127)","Binary_ınv(0,127,)","Trunc(100,200)","ToZero(127,255)","ToZero_Inv(127,255)"]

#Show the results
#Range function start from 0.
for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(thresholdList[i],'gray')
    plt.title(titleList[i])
    # Do not show values of axis
    #plt.xticks([]), plt.yticks([])

plt.show()
result=plt.show()
#Save the results
cv2.imwrite("ResultsOfThreshold.jpg", result)
cv2.imwrite()
#Close all windows
cv2.waitKey()
cv2.destroyAllWindows()