import cv2 as cv
import numpy as np

img = cv.imread("Photo/lena.jpg")
cv.imshow("Original", img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

canny = cv.Canny(blur, 127, 175)
cv.imshow("Edge Detection", canny)

contour, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print("Contour = %f" %(len(contour)))

cv.drawContours(blank, contour, -1, (0,0,255), 1)
cv.imshow('Contour Draw', blank)
cv.waitKey()