import cv2 as cv

img = cv.imread("Photo/lena.jpg")
cv.imshow("Original", img)

gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian Blur", gauss)

average = cv.blur(img, (3,3))
cv.imshow("Average Blur", average)

median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)