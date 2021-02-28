import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
blank[100:200, 400:500] = 255,0,0
cv.imshow("Blank", blank)

cv.rectangle(blank, (100,250), (300,300), (0,0,255), thickness=-1)
cv.imshow("Rectangle", blank)

cv.circle(blank, (100,150), 50, (255,0,0), thickness=-1)
cv.imshow("Circle", blank)

cv.putText(blank, '"Hi, Bro!!"', (200,200), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
cv.imshow("Text", blank)

cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
cv.imshow("Line", blank)

cv.waitKey(0)
