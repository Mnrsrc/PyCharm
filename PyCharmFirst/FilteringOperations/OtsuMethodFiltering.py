#import libraries
import  cv2
from matplotlib import pyplot as plt
import  numpy as np
#take an photo
image=cv2.imread('noisyFace.png',0)
#Apply the simple thresholding
_,simpleThresholding=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
#apply the otsu method filtering
_,otsuThreshold=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU+cv2.THRESH_OTSU)
#apply the Gaussian blur+otsu filtering
gaussianBlur=cv2.GaussianBlur(image,(5,5),0)
_,otsuBlur=cv2.threshold(gaussianBlur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#show result
images=[image,0,simpleThresholding,
        image,0,otsuThreshold,
        gaussianBlur,0,otsuBlur]
titles=["Original","Histogram","Simple_Thresh",
        "Original","Histogram","Gaussian_Blur",
        "Gaussian_Blur","Histogram","Otsu+Gaussian_Blur"]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]),plt.xticks([]),plt.yticks([])

plt.show()

#Close window
cv2.waitKey()
cv2.destroyAllWindows()