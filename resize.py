import cv2 as cv

def rescale_frame(frame, scale=1.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    print(width,height)

    dimension = (width, height)
    return cv.resize(frame, dimension)


img = cv.imread('Photo/lena.jpg')
frame2 = rescale_frame(img)
cv.imshow("Rescale Image", frame2)
cv.waitKey(0)