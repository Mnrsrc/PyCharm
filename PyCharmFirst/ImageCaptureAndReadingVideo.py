#import libraries
import cv2
#Read the video
#It means camera numbers. 0 camera because of the operation making on my computer.
video=cv2.VideoCapture(0)
video2=cv2.VideoCapture('smile2.3gp')
#Determinig how long seconds
while True:
    #refuse is a boolean value, if it is captured the image true, otherwise it is turned false
    refuse,imageVideo=video.read()
    refuse2,imageVideo2=video2.read()
    #Show the results
    cv2.imshow("Mywebcam",imageVideo)
    cv2.imshow("Rainy",imageVideo2)
    #ord('q') means represent to unicode character of 'q'
    if cv2.waitKey(25) & 0XFF==ord('q'):
        break


#Release the results
video.release()
video2.release()
#Finish
cv2.destroyAllWindows()

