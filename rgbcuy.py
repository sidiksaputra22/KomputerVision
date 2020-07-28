import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # yellow color
    low_yellow = np.array([25, 146, 190])
    upper_yellow = np.array([62, 174, 250])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, upper_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Yellow", yellow)
    key = cv2.waitKey(1)
    if key == 27:
        break
