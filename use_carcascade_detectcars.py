import cv2
import matplotlib.pyplot as plt

img = cv2.imread('resources/dpark/d1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier('resources/cars.xml')
# cascade = cv2.CascadeClassifier('resources/my_cascade.xml')
cars = cascade.detectMultiScale(gray, 1.1, 1)

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

car_size = cars
print(car_size)

cv2.imshow('IMG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Here we try to detect cars using a car cascade
"""
