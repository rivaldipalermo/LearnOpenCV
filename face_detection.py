import cv2 as cv

img = cv.imread('Photo/football.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')
face_detect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

for (x,y,w,h) in face_detect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

print(f'The number of face detected = {len(face_detect)}')
cv.imshow('Face Detection', img)

cv.waitKey(0)