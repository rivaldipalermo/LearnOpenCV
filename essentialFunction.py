import cv2 as cv

img = cv.imread("Photo/lena.jpg")
# cv.imshow("Original", img)

#Convert to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

#Edge Cascade
edge = cv.Canny(blur, 100, 150)
cv.imshow("Edge Cascade", edge)

#Dilating image
dilated = cv.dilate(edge, (7,7), iterations=3)
cv.imshow("Dilated", dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("Eroded", eroded)

#Resize
resized = cv.resize(img, (500,500))
cv.imshow("Resize", resized)

#Crop the image
crop = img[50:100, 80:400]
cv.imshow("Crop", crop)

cv.waitKey(0)