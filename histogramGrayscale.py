import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photo/lena.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blank = np.zeros((img.shape[:2]), dtype='uint8')

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 200, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Masked', mask)

#Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)