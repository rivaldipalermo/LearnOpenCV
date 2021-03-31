import cv2 as cv
import numpy as np

img = cv.imread("Photo/lena.jpg")
blank = np.zeros((img.shape[:2]), dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (70,70), (400,400), 255, -1)
mask_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("Preview Mask", mask_shape)

masked_image = cv.bitwise_and(img, img, mask=mask_shape)
cv.imshow("Masked Image", masked_image)
cv.waitKey()