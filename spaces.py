import cv2 as cv

img = cv.imread("Photo/lena.jpg")
cv.imshow("Original", img)

# plt.imshow(img)
# plt.show()

#Convert to grayscale
gray = cv.cvtColor(img,  cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

#Convert to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

#Convert to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

#Convert BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

cv.waitKey(0)

#Cant convert Grayscale to RGB,HSV,LAB directly