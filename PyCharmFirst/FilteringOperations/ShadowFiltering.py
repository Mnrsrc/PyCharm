#import libraries
import  cv2
from matplotlib import pyplot as plt
#take an image with shadow
image=cv2.imread("sayfa.jpg")
#Convert to gray
grayImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#Filtering simple
_,simpleThresh=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
_,simpleThreshGray=cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)
#Filtering adaptive
#gaussianAdaptive=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
gaussianAdaptiveGray=cv2.adaptiveThreshold(grayImage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
#Filtering otsu
#_,otsuFilter=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,otsuFilterGray=cv2.threshold(grayImage,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#Add to list
images=[image,grayImage,simpleThresh,simpleThreshGray,gaussianAdaptiveGray,otsuFilterGray]
titles=["Original","grayImage","simpleThresh","simpleThreshGray","gaussianAdaptiveGray","otsuFilterGray"]
#Show results
for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
"""cv2.imshow("image",image)
cv2.imshow("grayImage",grayImage)
cv2.imshow("simpleThresh",simpleThresh)
cv2.imshow("simpleThreshGray",simpleThreshGray)
cv2.imshow("gaussianAdaptiveGray",gaussianAdaptiveGray)
cv2.imshow("otsuFilterGray",otsuFilterGray)"""
#Close window
cv2.waitKey(0)
cv2.destroyAllWindows()