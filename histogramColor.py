import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photo/lena.jpg')
blank = np.zeros((img.shape[:2]), dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 200, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    color_hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(color_hist, color=col)
    plt.xlim([0,256])
    
plt.show()

cv.waitKey(0)