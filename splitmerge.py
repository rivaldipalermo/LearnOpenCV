import cv2 as cv
import numpy as np

img = cv.imread("Photo/lena.jpg")
cv.imshow("Original", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#split rgb
b,g,r = cv.split(img)
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)

print(img.shape)
print(img.shape[:1])


cv.imshow("Blank", blank)

cv.waitKey()