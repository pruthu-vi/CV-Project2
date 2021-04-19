import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('resources/dpark/d2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_gray = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)
edges = cv2.Canny(blur_gray, 50, 150, apertureSize=3)
edges2 = cv2.Canny(blur_gray, 25, 75, apertureSize=3)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 80, 15, 5)
for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('IMGo', img)
cv2.imshow('IMGE', edges)
#cv2.imshow('IMGE2', edges2)
cv2.waitKey(0)
cv2.destroyAllWindows()
