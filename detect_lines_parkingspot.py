import cv2
import numpy as np
import matplotlib.pyplot as plt


def find_lines(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = 5
    blur_gray = cv2.GaussianBlur(gray, (kernel, kernel), 0)

    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

    rho = 1
    theta = np.pi / 180
    threshold = 15
    min_line_length = 50
    max_line_gap = 20
    line_image = np.copy(img) * 0
    lines = cv2.HoughLinesP(edges, rho, theta, threshold,
                            np.array([]), min_line_length, max_line_gap)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)

    lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)

    return lines_edges


def main():
    #path = 'resources/dpark/sDQLM.png'
    path = 'resources/dpark/parkyllw.jpg'
    img = cv2.imread(path)
    imgF = find_lines(img)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

    plt.imshow(cv2.cvtColor(imgF, cv2.COLOR_BGR2RGB))
    plt.show()

    # cv2.imshow('Output', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


main()
