import cv2 as cv
import numpy as np

img = cv.imread('Photo/lena.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Advance Edge Detection
#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel', combine_sobel)

#Canny
canny = cv.Canny(gray, 120, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)