import cv2
import numpy as np
from matplotlib import pyplot as plt


#blue color is=[255,0,0]
image=cv2.imread("fractal.jpg")
#cv2.imshow("Fractal",image)
replicateImage=cv2.copyMakeBorder(image,250,250,250,250,cv2.BORDER_REPLICATE)
#cv2.imshow("Framed Picture with Replicate",replicateImage)
reflectedImage=cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_REFLECT)
#cv2.imshow("Framed picture with Reflect",reflectedImage)
reflected101Image=cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_REFLECT101)
#cv2.imshow("Framed Picture with Reflect101",reflected101Image)
wrappedImage=cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_WRAP)
#cv2.imshow("Framed Picture with Wrap",wrappedImage)
constantedImage=cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_CONSTANT)
#cv2.imshow("Framed Image with Constanted",constantedImage)
#FOR PUBLİC DİSPLAY
plt.subplot(231),plt.imshow(image,'pink'),plt.title("Original Picture")
plt.subplot(232),plt.imshow(replicateImage,'pink'),plt.title("Replicated")
plt.subplot(233),plt.imshow(reflectedImage,'pink'),plt.title("Reflected")
plt.subplot(234),plt.imshow(reflected101Image,'pink'),plt.title("Reflected101")
plt.subplot(235),plt.imshow(wrappedImage,'pink'),plt.title("Wrapped")
plt.subplot(236),plt.imshow(constantedImage,'pink'),plt.title("Constanted")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
