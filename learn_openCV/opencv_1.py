import cv2
import numpy as np
import matplotlib.pyplot as plt
print('Loaded !!!')

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('Resources/dpark/d1.jpg')
print(img.shape)
s = img.shape
w = s[0]
h = s[1]
print('Width is', w, '& Height is', h)

imgCanny = cv2.Canny(img, 150, 200)
imgDial = cv2.dilate(imgCanny, kernel, iterations=1)
imgErod = cv2.erode(imgDial, kernel, iterations=1)
imgResize = cv2.resize(img, (2*w, 2*h))
imgCropped = img[0:150, 10:350]

img2 = np.zeros((512, 512), np.uint8)
cv2.line(img2, (0, 0), (img2.shape[0], img2.shape[1]), (255, 0, 0), 2)
cv2.line(img2, (0, img2.shape[0]), (img2.shape[1], 0), (255, 0, 0), 2)
cv2.line(img2, (0, int(img2.shape[0]/2)),
         (int(img2.shape[1]/2), 0), (255, 0, 0), 2)

cv2.rectangle(img2, (0, 0), (123, 223), (255, 0, 0), cv2.FILLED)

cv2.circle(img2, (256, 256), 30, (255, 255, 0), 4)

cv2.putText(img2, "Hi PINK", (300, 100),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

# cv2.imshow('IMG Original', img)
# cv2.imshow('IMG Canny', imgCanny)
# cv2.imshow('IMG Dialate', imgDial)
# cv2.imshow('IMG Erode', imgErod)
# cv2.imshow('IMG Resized', imgResize)
# cv2.imshow('IMG Cropped', imgCropped)
cv2.imshow('IMG2', img2)
cv2.waitKey(0)

# plt.imshow(img)
# plt.show()
cv2. destroyAllWindows()
