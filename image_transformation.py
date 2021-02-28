import cv2 as cv
import numpy as np

img = cv.imread("Photo/lena.jpg")

cv.imshow("Original", img)

#Translation
def translation(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)

shift_img = translation(img, 100, 100)
cv.imshow("Translation", shift_img)

#Rotation
def rotation(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
        print(rotPoint)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotation(img, 90)
cv.imshow("Rotation", rotated)

#Resize
resized = cv.resize(img, (200,200))
cv.imshow("Resize", resized)

#Flipping
flip = cv.flip(img, 1)
cv.imshow("Flip", flip)

#Crop
cropped = img[100:200, 200:400]
cv.imshow("Croped", cropped)
cv.waitKey(0)