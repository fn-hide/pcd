import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os


filepath = 'c:/users/febri/pictures/pak aris.jpg'
# print(os.listdir(filepath))

img = cv.imread(filepath, 0)
imgHist = cv.calcHist([img], [0], None, [256], [0, 256])

print(np.unique(imgHist, return_counts=True))
print(np.unique(img, return_counts=True))

# plt.plot(imgHist)
plt.plot(imgHist)
plt.hist(img.ravel(), bins=256, range=(0, 256), fc='k', ec='k')
plt.show()

cv.imshow('tes', img)
cv.waitKey(0)
