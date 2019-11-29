#import libraries
import  cv2
#Opening the camera
camera=cv2.VideoCapture(0)

# Sizing the window/ #method1
#camera.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
#camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)


#Show the results
def show():
    while True:
        #refuse is boolean value
        refuse,videoCamera=camera.read()
        # Toning Gray the camera
        grayTone = cv2.cvtColor(videoCamera,cv2.COLOR_BGR2GRAY)
# Sizing the window/ #method2
#3. parameter
        refuse,camera.set(3,320)
#4. parameter
        refuse,camera.set(4,240)
        cv2.imshow("Video Camera", videoCamera)
        cv2.imshow("Gray Tone",grayTone)
        if cv2.waitKey(25) & 0XFF==ord('q'):
            break
    camera.release()
    # Finish

    cv2.destroyAllWindows()

def main():
    show()
if __name__=="__main__":
    main()
