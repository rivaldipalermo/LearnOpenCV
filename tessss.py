import cv2 as cv

capture = cv.VideoCapture(0)
while True:
    ret, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    haarcascade = cv.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')
    face_detect = haarcascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    for (x,y,w,h) in face_detect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    
    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()