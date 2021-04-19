import numpy as np
import cv2

print("ready")

cascade_link = 'https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_link)

img = cv2.imread('img.jpg', 0)

cv2.imshow("img", img)
cv2.waitKey(0)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (5, 25)
color = (255, 0, 0)

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img, 1.1, 5)
cv2.putText(img, "Number of {0} faces!".format(
    len(faces)), org, font, 1, color, 2)
