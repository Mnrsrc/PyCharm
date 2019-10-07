import cv2
import numpy as np
imageSeat=cv2.imread('seat.jpg')

print("Shape of Seat Picture:" + str(imageSeat.shape))
ROI=imageSeat[130:275,85:125]

imageSeat[130:275,230:270]=ROI
cv2.imshow('roi of Seat Image',ROI)
cv2.imshow("Seat",imageSeat)
cv2.waitKey(0)
cv2.destroyAllWindows()