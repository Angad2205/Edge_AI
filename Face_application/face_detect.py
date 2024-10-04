import cv2 as cv
import numpy as np
import os

cam = cv.VideoCapture(0)
while True:
    flag, frame = cam.read()
    if not flag:
        print("Failed to capture video")
        break

    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    har_cascade = cv.CascadeClassifier('har_cascade.xml')
    face = har_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in face:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)

    cv.imshow('live video', frame)

    if cv.waitKey(1) & 0xFF == ord('g'):
        break

cam.release()
cv.destroyAllWindows()