import cv2
import numpy as np
import matplotlib.pyplot as plt


def parking_spot_detect(img):
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    blur_gray = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)
    edges = cv2.Canny(blur_gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 80, 15, 5)

    for x1, y1, x2, y2 in lines[0]:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return img


def main():
    #path = 'resources/dpark/sDQLM.png'
    #path = 'resources/dpark/Blue_Disc_Parking_Area_Markings_Blue_Paint.JPG'
    path = 'resources/dpark/d1.jpg'
    img = cv2.imread(path)
    prk = parking_spot_detect(img)

    plt.imshow(prk)
    plt.show()


main()
