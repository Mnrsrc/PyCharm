#import libraries
import numpy as np
import cv2
def writeText():
    # Make a white matrix with 500*500 and  with colors
    image = np.zeros((500, 800, 3), np.uint8)
    # fill with white
    image.fill(255)
    # Font scale
    fontScala = 1.0
    # Color is red
    color = (0, 0, 255)
    # Write different type fonts
    fontFace = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(image, "1-FONT_HERSHEY_COMPLEX", (25, 40), fontFace, fontScala, color)

    color = (1, 1, 1)
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(image, "2-FONT_HERSHEY_COMPLEX_SMALL", (25, 60), fontFace, fontScala, color)

    color = (100, 100, 100)
    fontFace = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(image, "3-FONT_HERSHEY_DUPLEX", (25, 90), fontFace, fontScala, color)

    color = (200, 200, 200)
    fontFace = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(image, "4-FONT_HERSHEY_PLAIN", (25, 120), fontFace, fontScala, color)

    color = (250, 250, 0)
    fontFace = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(image, "5-FONT_HERSHEY_SCRIPT_COMPLEX", (25, 140), fontFace, fontScala, color)

    color = (0, 0, 0)
    fontFace = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(image, "6-FONT_HERSHEY_SCRIPT_SIMPLEX", (25, 160), fontFace, fontScala, color)

    color = (0, 255, 255)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, "7-FONT_HERSHEY_SIMPLEX", (25, 190), fontFace, fontScala, color)

    color = (255, 0, 255)
    fontFace = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(image, "8-FONT_HERSHEY_TRIPLEX", (25, 210), fontFace, fontScala, color)

    color = (255, 255, 0)
    fontFace = cv2.FONT_ITALIC
    cv2.putText(image, "9-FONT_ITALIC", (25, 240), fontFace, fontScala, color)
    # Show the results
    cv2.imshow("Font Types", image)
    # Finish
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def main():
    writeText()

if __name__=="__main__":
    main()

