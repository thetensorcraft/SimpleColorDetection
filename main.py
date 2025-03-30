# basic color(yellow) detection

import cv2 as cv
from util import get_limits # for limits 
from PIL import Image # for boundaries

# define the color
yellow = [0, 255, 255] # yellow in BGR colorspace

# load the webcam
cam = cv.VideoCapture(0)
while True:
    ret, frame = cam.read()
    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    lowerlimit, upperlimit = get_limits(color = yellow)
    mask = cv.inRange(hsvImage, lowerlimit, upperlimit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv.imshow("Frame", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
