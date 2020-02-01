#import libraries
import  cv2
from matplotlib import pyplot as plt
#Take an image, convert gray tone
image=cv2.imread('md_103_2.jpg',0)
#Apply the simple filter
refuse, imageFilter=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
#Apply the Gaussian C Filtering
imageGaussian=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#Apply the Mean C Filtering
imageMean=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,2)
#show result
images=[image,imageFilter,imageGaussian,imageMean]
titles=["Original","Simple Filter","Gaussian","Mean"]
for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.yticks([])
    plt.xticks([])
plt.show()




#close the window
cv2.waitKey()
cv2.destroyAllWindows()