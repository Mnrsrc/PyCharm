import cv2
import numpy as np

def main():
    image=cv2.imread('flowers.jpg')
    cv2.imshow("Original image",image)
    print("Original İmage:" + str(image.shape))
    resolution=720,720
    scaleMyPictureWeight=resolution[0]/image.shape[1]
    scaleMyPictureHeight=resolution[1]/image.shape[0]
    scale=min(scaleMyPictureHeight,scaleMyPictureWeight)
    print("Scale:" + str(scale))
    windowWeight=int(image.shape[1]*scale)
    windowHeight=int(image.shape[0]*scale)

    #for resizable in cv2
    cv2.namedWindow('Resizable Window',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Resizable Window2',windowWeight,windowHeight)
    #IT DOES NOT WORK CORRECTLY!!!
    print("Resize İmage:" + str(image.shape))
    cv2.imshow('Resize Window',image)
    cv2.waitKey()
    cv2.destroyAllWindows()
if __name__=="__main__":
        main()