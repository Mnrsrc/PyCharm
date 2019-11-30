#import libraries
import  cv2
#open the video camera/webcam
camera=cv2.VideoCapture(0)


#Show the results
def show():
    while True:
        refuse, videoCamera=camera.read()
        framed60=scale(videoCamera,60)
        cv2.imshow("Webcam",videoCamera)
        cv2.imshow("Scaling Webcam",framed60)
        if cv2.waitKey(10)& 0XFF==ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
#Setting the resolution in different formats
def resolution1080p():
    #Width
    camera.set(3,1920)
    #height
    camera.set(4,1080)
def determineResolution(width,height):
    camera.set(3,width)
    camera.set(4,height)
def resolution720p():
    camera.set(3,1280)
    camera.set(4,720)
def resolution480p():
    camera.set(3,640)
    camera.set(4,480)
# Image Scaling
def scale(videoCamera,percent=75):
    width=int(videoCamera.shape[1]*percent/100)
    height=int(videoCamera.shape[0]*percent/100)
    dimensionFrame=(width,height)
    return cv2.resize(videoCamera,dimensionFrame,interpolation=cv2.INTER_AREA)



def main():
    resolution1080p()
    #determineResolution()
    #resolution720p()
    #resolution480p()
    show()

if __name__=="__main__":
    main()