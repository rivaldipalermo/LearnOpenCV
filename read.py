import cv2 as cv

capture = cv.VideoCapture('Video/bandung.mp4')

while True:
    isTrue, frame = capture.read()
    cv.rectangle(frame, (100,100), (250,250), (0,255,0), thickness=3)
    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()