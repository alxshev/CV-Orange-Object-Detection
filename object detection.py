import cv2
import numpy as np

MIN_COLOR_THRESH = np.array([0, 180, 20])
MAX_COLOR_THRESH = np.array([50, 255, 200])

# read in video
cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # map to HSV for easier color specification

    # get parts of image within specified color threshold
    mask = cv2.inRange(hsv, MIN_COLOR_THRESH, MAX_COLOR_THRESH)
    print(mask)

    # Returns frame && mask (Matlab-style logical array and operator)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # Show all 3 images
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(0)
cv2.destroyAllWindows()