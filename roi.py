import cv2

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    #ROI
    x1 = 400
    y1 = 30

    x2 = 600
    y2 = 200
    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 1)

    roi = frame[ y1:y2 , x1:x2 ]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _,roi = cv2.threshold(roi, 132, 255, cv2.THRESH_BINARY)

    cv2.imshow("Frame",frame)
    cv2.imshow("ROI", roi)
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break
    elif interrupt & 0xFF == ord('c'):
        cv2.imwrite("ResultROI.jpg", roi)

cap.release()
cv2.destroyAllWindows()