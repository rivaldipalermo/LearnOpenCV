import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    ret, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')
    face_detect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x,y,w,h) in face_detect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)

    cv.imshow('Face Detection', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()