import cv2 as cv

img = cv.imread('Photo/lena.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Simple Threshold
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresh', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Invert Simple Thresh', thresh_inv)

#Adaptive Threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 1)
cv.imshow('Adaptive Threshold', adaptive_thresh)

cv.waitKey(0)