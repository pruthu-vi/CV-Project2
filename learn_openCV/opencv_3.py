import cv2
import numpy as np
import matplotlib.pyplot as plt
print('Loaded !!!')

img = cv2.imread('Resources/file-shapes-for-kids-1592568510.jpg')

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

meStack = np.hstack((np.vstack((img, img))))

# So find the funcion that
# stackImages():

cv2.imshow('IMG', meStack)
cv2.waitKey(0)

# plt.imshow(img)
# plt.show()
cv2. destroyAllWindows()
