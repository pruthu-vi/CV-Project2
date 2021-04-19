import cv2
import numpy as np
import matplotlib.pyplot as plt
print('Loaded !!!')

img = cv2.imread('Resources/file-shapes-for-kids-1592568510.jpg')

width, height = 250, 350
pts1 = np.float32([[266, 233], [268, 48], [428, 239], [410, 48]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('IMG', imgOut)
cv2.waitKey(0)

# plt.imshow(img)
# plt.show()
cv2. destroyAllWindows()
