import cv2
import matplotlib.pyplot as plt

image = cv2.imread("lena.jpg")
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,biner = cv2.threshold(image_grayscale,110,255,cv2.THRESH_BINARY)
plt.hist(image_grayscale.ravel(),256,[0,256])
plt.show()

cv2.imshow("Frame",image)
cv2.imshow("Frame Grayscale",image_grayscale)
cv2.imshow("Frame Threshold",biner)

cv2.waitKey(0)
cv2.destroyAllWindows()